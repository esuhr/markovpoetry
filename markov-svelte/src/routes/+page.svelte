<script>
    import { onMount, onDestroy } from 'svelte';
    // import { words, transitions, loadPoems } from '$lib/poems.js'
    // import { shortGenerator } from '$lib/helpers.js'

    let textinput;
    // let corpuswords, corpustransition;
    let placeholder = 'block'
    // let startword;
    let generated;


    onMount( async() => {
        const url = 'http://127.0.0.1:5000/init'
        const options = {method: 'POST', headers: {'Content-Type': 'application/json',}, mode: 'cors'}
        const res = await fetch(url, options);
        console.log(res.message)
    })

    $: startword = '';

    const togglePlaceholder = () => {
        placeholder = 'none';
    }

    const getText = async (e) => {
        if (e.key === ' ') {
            startword = textinput.innerText.split(' ').slice(-1)[0];
            console.log(startword)

            const url = `http://127.0.0.1:5000/generate?start_word=${startword}&num_words=20`
            const options = {method: 'POST', headers: {'Content-Type': 'application/json',}, mode: 'cors'}
            const res = await fetch(url, options);
            const json = await res.json();
            generated = json.message;
        }
    }

</script>
<div class="page-container">
    <div class="text-container">
        <div class='text-input' contenteditable="true" bind:this={textinput} on:focus={togglePlaceholder} on:keypress={getText} role="textbox" tabindex="">
            {#if placeholder === 'block'}
                <span class='placeholder' style='display:{placeholder};'>Start writing...</span>
            {/if}
        </div>
        {#if generated}
            <span class='generated'>{generated}</span>
        {/if}
    </div>
</div>


<style>
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital@0;1&display=swap');

    :global(body) {
        margin: 0;
        padding: 0;
        overflow: hidden;
        height: 100vh;
        width: 100vw;
    }
    .page-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        background-color: #f2f0ec;
        height: 100%;
        width: 100%;
    }

    .placeholder {
        color: #999;
        font-style: italic;
    }
    /* .filter-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 25%;
        height: 100%;
    }
    .filter {
        width: 80%;
        padding-top: 4rem;
    } */
    .text-container {
        height: 100%;
        width: 50%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: 0;
    }
    .text-input {
        width: 80%;
        height: 60%;
        padding: 4rem;
        font-family: 'EB Garamond', serif;
        font-size: 32px;
        color: #333;
        border: none;
        box-shadow: 0px 0px 4px 0px #33333326;
        background-color: #f2f0ec;
        caret-shape: block;
        caret-color: #333;
    }
    .text-input:focus {
        outline: none;
    }
    .text-input::selection {
        background-color: #333;
        color: #f2f0ec;
    }
    .text-input::placeholder {
        color: #999;
        font-style: italic;
    }
    .generated {
        padding-top: 1rem;
        color: #666;
        font-style: italic;
    }
</style>