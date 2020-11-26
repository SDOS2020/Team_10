<script context="module">
    export async function preload(page, session) {
        const res = await this.fetch(`profileDetails/`);
        const userDetails = await res.json();

        return { userDetails };
    }
</script>  
<script>
    export let userDetails;
    console.log(userDetails)
</script>


<style>
</style>

<section class="main">
Hi <span class="name">{userDetails.name}</span> you have <span class="numProjects">2</span> projects.
</section>

