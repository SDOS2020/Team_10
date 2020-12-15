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
	border-radius: 5px;
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
$spacing: 1rem;
$themeColor: #63B8FF;
$backColor: #ddd;
$textShadow: rgba(black, 0.35) 1px 1px 1px;
.progress--circle {
    position: relative;
    display: inline-block;
    margin: $spacing;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background-color: $backColor;
        &:before {
        content: '';
        position: absolute;
        top: 15px;
        left: 15px;
        width: 90px;
        height: 90px;
        border-radius: 50%;
        background-color: white;
    }
    &:after {
        content: '';
        display: inline-block;
        width: 100%;
        height: 100%;
        border-radius: 50%; 
        background-color: $themeColor;
    }
}

.progress__number {
    position: absolute;
    top: 50%;
    width: 100%;
    line-height: 1;
    margin-top: -0.75rem;
    text-align: center;
    font-size: 1.5rem;
    color: #777;
}
$step: 5;
$loops: round(100 / $step);
$increment: 360 / $loops;
$half: round($loops / 2);
@for $i from 0 through $loops {
    .progress--bar.progress--#{$i * $step}:after {
        width: $i * $step * 1%;
    }
    .progress--circle.progress--#{$i * $step}:after {
        @if $i < $half {
            $nextDeg: 90deg + ($increment * $i);
            background-image: linear-gradient(90deg, $backColor 50%, transparent 50%, transparent), linear-gradient($nextDeg, $themeColor 50%, $backColor 50%, $backColor);
        }
        @else {
            $nextDeg: -90deg + ($increment * ($i - $half));
            background-image: linear-gradient($nextDeg, $themeColor 50%, transparent 50%, transparent), linear-gradient(270deg, $themeColor 50%, $backColor 50%, $backColor);
        }
    }
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
                <div class="progress--circle progress--25">
                    <div class="progress__number">25%</div>
                </div>

                <button class="button">EDIT</button>
            {:else}
                <p class="sub">
                    Your profile seems to be incomplete, choose any of the two options below to continue...
                </p>

                <a class="button" href="/mentoring/apply">APPLY FOR MENTOR</a>
                <a class="button" href="/profile/complete/">COMPLETE PROFILE</a>
                
            {/if}
		
		
	</div>
</section>
