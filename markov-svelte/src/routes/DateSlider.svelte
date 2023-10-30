<script>
    import RangeSlider from 'svelte-range-slider-pips';
    let values = [1000, 2023];
    console.log(values)
</script>

<div class='slider-container'>
    <RangeSlider 
        id='rangeSlider'
        range=true
        float='true'
        min={1000}
        max={2023}
        step={1}
        first='label'
        last='label'
        bind:values={values}
    />
    <span class='years-label'>Select years</span>
</div>


<style>
    :global(#rangeSlider) {
        font-size: .3rem;
        width: 100%;
    }
    :global(#rangeSlider > .rangeHandle > .rangeFloat) {
        font-size: .8rem;
        background-color: rgba(0,0,0,0);
        color: #999;
    }
    .slider-container {
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .years-label {
        font-size: .8rem;
        font-style: italic;
        color: #999;
    }
</style>

<!-- 
.rangeSlider {}                /* the main slider background track */
.rangeSlider.vertical {}       /* if slider is vertical */
.rangeSlider.focus {}          /* if slider is focussed */
.rangeSlider.range {}          /* if slider is a range */
.rangeSlider.min {}            /* if slider is a min-range */
.rangeSlider.max {}            /* if slider is a max-range */
.rangeSlider.pips {}           /* if slider has visible pips */
.rangeSlider.pip-labels {}     /* if slider has labels for pips */
.rangeSlider.hoverable {}      /* if slider can trigger hover effects */
/* slider handles */
.rangeSlider > .rangeHandle {}                 /* positioned wrapper for the handle/float */
.rangeSlider > .rangeHandle.active {}          /* if a handle is active in any way */
.rangeSlider > .rangeHandle.press {}           /* if a handle is being pressed down */
.rangeSlider > .rangeHandle > .rangeNub {}     /* the actual nub rendered as a handle */
.rangeSlider > .rangeHandle > .rangeFloat {}   /* the floating value above the handle */
/* slider range */
.rangeSlider > .rangeBar {}                    /* the range between the two handles */
/* slider pips */
.rangeSlider > .rangePips {}                   /* the container element for the pips */
.rangeSlider > .rangePips.focus {}             /* if slider is focussed */
.rangeSlider > .rangePips.vertical {}          /* if slider is vertical */
.rangeSlider > .rangePips.hoverable {}         /* if the pips allow hover effect */
.rangeSlider > .rangePips > .pip {}            /* an individual pip */
.rangeSlider > .rangePips > .pip.first {}      /* the first pip on the slider */
.rangeSlider > .rangePips > .pip.last {}       /* the last pip on the slider */
.rangeSlider > .rangePips > .pip.selected {}   /* if a pip is selected */
.rangeSlider > .rangePips > .pip.in-range {}   /* if a pip is somewhere in the range */
.rangeSlider > .rangePips > .pip > .pipVal {} -->