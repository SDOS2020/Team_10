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
    text-align: left;
    font-size: .8rem;
}
form {
    display: flex;
    flex-direction: column;
}

form>* {
    margin: 5px 10px;
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
<script>

</script>

<section class="main">
	<div class="wrapper">
		<h1>Complete your profile.</h1>

		<form action="/completeProfile" method="POST">
            <input type="text" name="last_name" placeholder="Last name" required class="input-border" value="">
			<input type="number" name="duration" placeholder="Average time spent on learning (hours)" required class="input-border" value="3">
            <select name="qualification" id="qualification" class="input-border" required>
                <option value="B.Tech CSE">B.Tech CSE</option>
                <option value="B.Tech ECE">B.Tech ECE</option>
                <option value="B.Tech (Other)">B.Tech (Other)</option>
                <option value="M.Tech CSE">M.Tech CSE</option>
                <option value="M.Tech ECE">M.Tech ECE</option>
                <option value="M.Tech (Other)">M.Tech (Other)</option>
            </select>
            <input type="text" name="institute" placeholder="Institute" class="input-border" required>
            <input type="text" name="interests" placeholder="Interests (career building, ML)" class="input-border" required>
            
            <input type="submit" value="COMPLETE PROFILE">
		</form>
		
		
	</div>
</section>
