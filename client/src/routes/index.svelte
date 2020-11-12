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
	opacity: .7;
}
form {

    display: inline-flex;
    // flex-direction: row;
}

form>* {
    margin: 10px 5px 0 0;
}

form .input-border {
    padding: 10px 10px;
    border: 1px solid #999;
    background: #fff;
    font-size: 14px;
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
</style>

<svelte:head>
	<title>WebMP : Home</title>
</svelte:head>

<section class="main">
	<div class="wrapper">
		<h1>WebMP: Mentor growth</h1>
		<p>Some small description to make people feel inspired and attracted towards the service. Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum qui itaque omnis ut ex alias ducimus.</p>

		<form action="/register/" method="POST">
			<input type="text" name="firstName" placeholder="First name" required class="input-border">
			<input type="email" name="email" placeholder="Email address" required class="input-border">
			<input type="password" name="password" placeholder="Password" required class="input-border">

			<input type="submit" value="JOIN WEBMP">
		</form>
	</div>
</section>
