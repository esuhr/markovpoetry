<script>
    let text = ''
</script>

<div class='author-container'>
    <input class='author-search' type='text' value={text} />
    <span class='author-label'>Search by author</span>
</div>

<style>
    .author-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .author-search {
        font-family: 'EB Garamond', serif;
        font-size: 1rem;
        color: #999;
        border: none;
        border-bottom: 1px solid #999;
        background-color: rgba(0,0,0,0);
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
        outline: none;
    }
    .author-label {
        font-size: .8rem;
        font-style: italic;
        color: #999;
        padding-top: 1rem;
    }
</style>