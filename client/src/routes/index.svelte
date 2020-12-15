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

</style>

<svelte:head>
	<title>WebMP : Home</title>
</svelte:head>

<section class="main">
	<div class="wrapper">
		<h1>WebMP: Mentor growth</h1>
		<p>Some small description to make people feel inspired and attracted towards the service. Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum qui itaque omnis ut ex alias ducimus.</p>

		<form action="/register" method="POST">
			<input type="text" name="first_name" placeholder="First name" required class="input-border">
			<input type="email" name="email" placeholder="Email address" required class="input-border">
			<input type="password" name="password" placeholder="Password" required class="input-border">

			<input type="submit" value="JOIN WEBMP">
		</form>

		<p class="s">
			Already have an account? <a href="/login">Login here</a>
		</p>
	</div>
</section>
