<style lang="scss">
.main {
	position: absolute;
	left: 50%;

	top: 50%;
	transform: translate(-50%, -50%);
}

.wrapper {
	width: 80vmin;
	background: rgba(#fff, .9);
	border-radius: 5px;
	box-shadow: 0 0 6px rgba(#000, 0.2);
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


.button {
	background: #333;
    border: none;
    padding: 10px 10px;
    color: #fff;
    letter-spacing: 1px;
    cursor: pointer;
    width: 60px;
    position: relative;
    font-size: .8rem;
}

.sub {
    font-size: 1rem;
    opacity: .8;
    margin-bottom: 20px; 
}
.badge {
    font-size: .6rem;
    text-transform: uppercase;
    padding:3px 10px;
    border-radius: 50px;
    color: #808080;
}

.qualification {
    background: #2ecc71;
}

.user_type {
    background: #808080;
}
</style>

<svelte:head>
	<title>Profile</title>
</svelte:head>

<script context="module">
    import { authCheck } from '../../utils/user';
    export async function preload(page, session) {
        authCheck(session, this.redirect);
        const res = await this.fetch(`profileDetails/`);
        const userDetails = await res.json();
        return { userDetails };
    }
</script>  
<script>
    export let userDetails;
    let profileComplete = false;
    let user_type = 'Mentee';
    if (userDetails.user_type === 'MR') {
        user_type = 'Mentor'
    }
    if (userDetails.user_type==='MT' && userDetails.organization!=='' && userDetails.requirement!=='') {
        profileComplete = true;
    } 
    console.log(userDetails)
</script>

<section class="main">
	<div class="wrapper">
		<h1>Hi, {userDetails.first_name} 
        </h1>
            <span class="badge qualification">{userDetails.qualification}</span>
            <span class="badge user_type">{user_type}</span>

            {#if profileComplete}
                <button class="button">EDIT</button>
            {:else}
                <p class="sub">
                    Your profile seems to be incomplete, choose any of the two options below to continue...
                </p>

                <a class="button">APPLY FOR MENTOR</a>
                <a class="button">COMPLETE PROFILE</a>
                
            {/if}
		
		
	</div>
</section>
