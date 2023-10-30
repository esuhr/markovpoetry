export const findAuthors = (poems) => {
    const authors = poems.map(poem => poem.poem_clean);
    return [...new Set(authors)];
}

export const filterByDate = (poems, dates, authors) => {
    const filteredDates = poems.filter(poem => poem.date <= dates[0] && poem.date <= dates[1]);
    const filteredAuthors = filteredDates.filter(poem => authors.includes(poem.author));
    return filteredAuthors;
}

export const createCorpus = (poems) => {
    const corpus = poems.map(poem => poem.poem_clean);
    const text = corpus.join('\n');
    const words = text.split(' ');
    const transition = new Map();
  
    for (let i = 0; i < words.length - 1; i++) {
        const current = words[i];
        const next = words[i + 1];
        if (!transition.has(current)) {
            transition.set(current, []);
        }
        transition.get(current).push(next);
    }
  
    return [words, transition];
}

const choice = (arr) => {
    return arr[Math.floor(Math.random() * arr.length)];
}

export const shortGenerator = (words, transition, start_word) => {
    if (!words.includes(start_word)) {
        return null;
    }
  
    for (let i = 0; i < words.length - 2; i++) {
        const w0 = words[i];
        const w1 = words[i + 1];
        const w2 = words[i + 2];
        if (!transition.has(`${w0},${w1}`)) {
            transition.set(`${w0},${w1}`, []);
        }
        transition.get(`${w0},${w1}`).push(w2);
    }
  
    const i = words.indexOf(start_word);
    let w0 = words[i];
    let w1 = words[i + 1];
    let w2 = words[i + 2];
  
    const newwords = [];
    for (let j = 0; j < 20; j++) {
        [w0, w1, w2] = [w1, w2, choice(transition.get(`${w1},${w2}`))];
        newwords.push(w2);
    }
  
    return newwords.join(' ');
  }