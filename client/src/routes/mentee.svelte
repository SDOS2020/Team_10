<style lang="scss">
.main {
	position: absolute;
	left: 50%;

	top: 50%;
	transform: translate(-50%, -50%);
}

.wrapper {
	width: 80vmin;
	background: rgba(#15171B, 1);
	
	box-shadow: 0 0 6px rgba(#000, 0.07);
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
    border: 1px solid #f20c40;
    background: transparent;
    font-size: 14px;
    color: #fff;
    font-family: var(--font-default);
    letter-spacing: 1px;
}

form input[type='submit'] {
    background: #333;
    border: none;
    padding: 10px 10px;
    color: #fff;
    letter-spacing: 1px;
    cursor: pointer;
}

.button {
	background: #333;
    border: none;
    padding: 10px 10px;
    color: #fff;
    letter-spacing: 1px;
    cursor: pointer;
    position: relative;
    left: 510px;
}
</style>

<svelte:head>
	<title>Mentee</title>
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
		<h1>Mentee</h1>
		<p><span class="name">{userDetails.name}</span></p>

		<form action="/acceptMentee" method="POST">
			<input type="submit" value="ACCEPT">
		</form>

		<form action="/nextMentee" method="POST">
			<button class="button" type="submit" formmethod="POST">NEXT</button>
		</form>
		
		
	</div>
</section>
