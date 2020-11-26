<style lang="scss">
.main {
	position: absolute;
	left: 50%;

	top: 50%;
	transform: translate(-50%, -50%);
}

.wrapper {
	width: 80vmin;
	background: rgba(#fff, .6);
	border-radius: 10px;
	box-shadow: 0 0 6px rgba(#000, 0.2);
	padding: 2rem 0rem 2rem 2rem;
}

h1{
	font-size: 2rem;
	text-transform: uppercase; 
}
p {
    margin: 10px 0;
	opacity: .7;
}

form {

    display: inline-flex;
    // flex-direction: row;
}

form>* {
    margin: 10px 5px 10px 0;
}

form .input-border {
    padding: 10px 10px;
    border: 1px solid #999;
    background: #fff;
    font-size: 14px;
    font-family: var(--font-default);
    letter-spacing: 1px;
}

.button {
	background: #333;
    border: none;
    padding: 10px 10px;
    color: #fff;
    letter-spacing: 1px;
    cursor: pointer;
    width: 60px;
    position: relative;
    left: 600px;
}
</style>

<svelte:head>
	<title>Profile</title>
</svelte:head>

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

<section class="main">
	<div class="wrapper">
		<h1>Profile Details</h1>
		<p><span class="name">{userDetails.name}</span></p>

		<form action="/editprofile" method="POST">
			<button class="button" type="submit" formmethod="POST">EDIT</button>
		</form>
		
		
	</div>
</section>
