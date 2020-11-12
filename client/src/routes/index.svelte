<style lang="scss">
.main {
	position: absolute;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);
}

.wrapper {
	width: 80vmin;
}
</style>

<svelte:head>
	<title>WebMP : Home</title>
</svelte:head>

<section class="main">
	<div class="wrapper">
		<h1>WebMP: Mentor growth</h1>
		<p>Some small description to make people feel inspired and attracted towards the service.</p>

		<form action="/register/" method="POST">
			<input type="text" name="firstName" placeholder="First name" required class="input-border">
			<input type="email" name="email" placeholder="Email address" required class="input-border">
			<input type="password" name="password" placeholder="Password" required class="input-border">

			<input type="submit" value="JOIN WEBMP">
		</form>
	</div>
</section>
