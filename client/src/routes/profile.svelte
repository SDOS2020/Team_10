<script context="module">
    export async function preload(page, session) {
        const res = await this.fetch(`profileDetails/`);
        const userDetails = await res.json();

        return { userDetails };
    }
</script>  
<script>
    console.log(userDetails)
    export let userDetails;
</script>


<style>
</style>

<section class="main">
{userDetails.name}
</section>

