import { writable } from 'svelte/store';
import { createCorpus } from './helpers.js';

const words = writable([]);
const transitions = writable([]);


const loadPoems = async () => {
    let corpuswords, corpustransitions;
    const url = 'http://127.0.0.1:5000/poems'
    const options = {method: 'GET', headers: {'Content-Type': 'application/json',}, mode: 'cors'}

    const res = await fetch(url, options);
    const data = await res.json();

    [corpuswords, corpustransitions] = createCorpus(data);
    words.set(corpuswords);
    transitions.set(corpustransitions);
}

export { loadPoems, words, transitions }