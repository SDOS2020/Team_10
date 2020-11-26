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
		
        <h3>edit profile</h3>
		<form action="/save_profile/" method="POST">
			<input type="name" name="name" placeholder="Name" required class="input-border">
			<input type="location" name="location" placeholder="City" required class="input-border">
			<input type="college" name="college" placeholder="College Name" required class="input-border">
			<input type="mm" name="mm" placeholder="Mentor or Mentee" required class="input-border">
			

			<input type="submit" value="SAVE">
		</form>
        
	</div>
</section>
