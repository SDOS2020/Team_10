
<style lang="scss">
    .style-one {
        background: rgb(15,16,19);
        background: linear-gradient(90deg, rgba(21,23,27,1) 0%, rgba(15,16,19,1) 50%, rgba(21,23,27,1) 100%);
    }
    .style-two {
        background: rgb(15,16,19);
        background: linear-gradient(45deg, rgba(21,23,27,1) 0%, rgba(15,16,19,1) 20%, rgba(21,23,27,1) 100%);
    }
    .style-three {
        background: rgb(15,16,19);
        background: linear-gradient(90deg, #15171b 0%, #0f1013 70%, #15171b 100%);
    }
    .card {
        padding: 1.5rem .5rem;
        border-radius: 10px;
        box-shadow: 0 0 5px rgba(#000,.4);
        margin-bottom: 10px;
        width: 90%;
        position: relative;
        top: 0px;
        transition: all .2s ease-in-out;

        display: grid;
        grid-template-columns: 0.6fr 1.4fr;
        grid-template-rows: 1fr;
        gap: 0px 0px;
        grid-template-areas:
        "left right";
        align-items: center;
    }

    .card:hover {
        top: -3px;
        box-shadow: 0 3px 5px rgba(#000, .5);
    }
    h1 {
        opacity: .8;
    }
    h3 {
        font-size: .8rem;
        text-transform: uppercase;
        opacity: .6;
        font-weight: normal;
    }
    .data {
        opacity: 1;
        font-size: 2rem;
    }


    .left { grid-area: left; text-align: center;}
    .right { grid-area: right; }

    .panel {
      padding: 0 18px;
      background-color: white;
      display: none;
      overflow: hidden;
    } 

</style>    

<script>
    export let title,  subtext, link, styleNumber, data, ispost = true, acc = false;
    import { slide } from 'svelte/transition';
    let visible = true;
    export let sections = [
        {
            id: 1,
            title: "Section 1",
            content: ["comment 1", "comment 2", "comment 3"],
            active: false,
        },
        {
            id: 2,
            title: "Section 2",
            content: ["comment 1"],
            active: false,
        },
        {
            id: 3,
            title: "Section 3",
            content: ["comment 1"],
            active: false,
        }
    ]
    
    const expand = (section) => {
        sections = sections.map(s => {
//          s.active = false
            
            if (s.id === section.id) {
                if (s.active == false) s.active = true
                else s.active = false
            }
            return s
        })
    }
</script>

{#if !acc}
<a href="{link}">
    {#if ispost}
    <section class="card style-{styleNumber}">
        <div class="left">
            <span class="data">{data}</span>
        </div>
        <div class="right">
            <h1 class="title">{title}</h1>        
            <h3 class="subtext">
                {subtext}
            </h3>
            
        </div>
    </section>
    {:else}
    <section class="card style-{styleNumber}">
        <div class="left">
            <h1 class="title">{title}</h1>
        </div>
        <div class="right">
                    
            <h3 class="subtext">
                {subtext}
            </h3>
            
        </div>
    </section>
    

    {/if}
</a>


{:else}
<a>
{#each sections as section}

    <section class="card style-{styleNumber}" on:click={() => expand(section) }>
        <div class="left">
            <h1 class="title">{title}</h1>
        </div>
        <div class="right">
                    
            <h3 class="subtext">
                {subtext}
            </h3>
            
        </div>
        {#if section.active}
        <div class="slider" transition:slide>
            {#each section.content as comment}
                <p>{comment}<br></p>
            {/each}
        </div>
        {/if}
    </section>
    {/each}
</a>
{/if}