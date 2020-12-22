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
    padding: 2rem;
    
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr;
    gap: 0px 0px;
    grid-template-areas:
                    "left right";
    
    align-items: center;
}
form>* {
    margin: 5px 10px 5px 0;
    width: 100%;
}

.left { grid-area: left; }
.right { 
    grid-area: right; padding: 0 1rem 0 2rem; 
    p.lead {
        font-size: .8rem;
    }
}


</style>

<section class="main">
    <div class="wrapper">
        <div class="left">
            <form action="/applyMentor" method="POST">
            <input type="text" name="last_name" placeholder="Last name" required class="input-border" value="">

            <div class="input-group">
                <label for="duration">Time available for mentoring (hours)</label>
                <input type="number" name="duration" placeholder="Average time spent on learning (hours)" required class="input-border" value="3">
            
            </div>            

            <div class="input-group">
                <label for="qualification">Current qualification</label>
                <select name="qualification" id="qualification" class="input-border" required>
                    <option value="Industry (B.Tech)">Industry (Bachelors)</option>
                    <option value="Industry (M.Tech)">Industry (Masters)</option>
                    <option value="Industry (PhD)">Industry (Doctorate)</option>
                    <option value="Industry (Other)">Industry (Other)</option>
                    <option value="Professor (Masters)">Professor (Masters)</option>
                    <option value="Professor (Doctorate)">Professor (Doctorate)</option>
                    <option value="Professor (Other)">Professor (Other)</option>
                </select>
            </div>
            <input type="text" name="organization" placeholder="Institute/Organization" class="input-border" required>
            <input type="text" name="requirement" placeholder="Teaching areas (career building, ML)" class="input-border" required>
            <div class="input-group">
                <label for="cv">Curriculam Vitae</label>
                <input type="file" placeholder="Curriculam vitae" class="input-border">
            </div>
            
            <input type="submit" value="SUBMIT APPLICATION">
		</form>
        </div>
        
        <div class="right">
            <h1>Apply for mentoring</h1>
            <p class="lead">
                Submit interests, necessary documentation and the listed teaching requirements.
                Your application will be evaluated, and you will be notified of your acceptance through e-mail.
            </p>
        </div>
    </div>
</section>


<script>
</script>


