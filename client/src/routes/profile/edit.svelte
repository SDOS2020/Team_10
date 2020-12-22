<style lang="scss">
.main {
	position: absolute;
	left: 50%;

	top: 50%;
	transform: translate(-50%, -50%);
}

.wrapper {
	width: 40vmin;
	background: rgba(#15171B, 1);
	
	box-shadow: 0 0 6px rgba(#000, 0.07);
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
