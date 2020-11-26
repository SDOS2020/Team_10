<style lang="scss">
.main {
	position: absolute;
	left: 50%;

	top: 50%;
	transform: translate(-50%, -50%);
}

.wrapper {
	width: 40vmin;
	background: rgba(#fff, .6);
	border-radius: 10px;
	box-shadow: 0 0 6px rgba(#000, 0.2);
	padding: 2rem;
}

h3{
	text-transform: uppercase; 
}
p {
    text-align: center;
    margin-top: 10px;
}
form {
    display: flex;
    flex-direction: column;
}

form>* {
    margin: 10px;
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
    border: none !important;
    outline: none !important;
    padding: 10px 10px;
    color: #fff;
    letter-spacing: 1px;
    cursor: pointer;
    border-radius: 5px;
}
</style>

<svelte:head>
	<title>WebMP : Home</title>
</svelte:head>

<section class="main">
	<div class="wrapper">
		
        <h3>login to webmp</h3>
		<form action="/login/" method="POST">
			<input type="email" name="email" placeholder="Email address" required class="input-border">
			<input type="password" name="password" placeholder="Password" required class="input-border">

			<input type="submit" value="LOGIN">
		</form>
        <p class="s">
			Don't have an account? <a href="/">Register</a>
		</p>
	</div>
</section>
