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

</style>
<script>

</script>

<section class="main">
	<div class="wrapper">
		<h1>Complete your profile.</h1>

		<form action="/completeProfile/" method="POST">
            <input type="text" name="last_name" placeholder="Last name" required class="input-border" value="">
			<div class="input-group">
                <label for="duration">Time learning/working under a mentor (hrs)</label>
                <input type="number" name="duration" placeholder="Average time spent on learning (hours)" required class="input-border" value="3">
			</div>
            <div class="input-group">
                <label for="qualification">Current qualification</label>
                <select name="qualification" id="qualification" class="input-border" required>
                    <option value="B.Tech CSE">B.Tech CSE</option>
                    <option value="B.Tech ECE">B.Tech ECE</option>
                    <option value="B.Tech (Other)">B.Tech (Other)</option>
                    <option value="M.Tech CSE">M.Tech CSE</option>
                    <option value="M.Tech ECE">M.Tech ECE</option>
                    <option value="M.Tech (Other)">M.Tech (Other)</option>
                </select>
            </div>
            <input type="text" name="organization" placeholder="Institute" class="input-border" required>
            <input type="text" name="requirement" placeholder="Interests (career building, ML)" class="input-border" required>
            
            <input type="submit" value="COMPLETE PROFILE">
		</form>
		
		
	</div>
</section>
