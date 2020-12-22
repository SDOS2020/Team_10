<style lang="scss">

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




.sub {
    font-size: 1rem;
    opacity: .8;
    margin-bottom: 20px; 

}

.badges {
    float: left;
    width: 100%;
    margin-bottom: 1em;
}
.badge {
    font-size: .6rem;
    text-transform: uppercase;
    padding:3px 10px;
    border-radius: 50px;
    color: #fff;
    display: inline-block;

}

.qualification {
    background: lighten(#467E84, 5%);
}

.user_type {
    background: #73645D;
}
.action-mini_wrapper {

    width: 100%;
    // padding: 1rem;
    margin-top: 1rem;
}

.greet {
   background: rgba(#15171b, 1);
    padding: 2rem 1rem; 
}

.container {
    margin-top: 1.5rem;
    width: 100%;
    h1 {
        font-size: 1.5rem;
    }
}

.container2 {
    float: left;
    display: inline-block;
    vertical-align: top;
    width: 33%;

}
</style>

<svelte:head>
	<title>Profile</title>
</svelte:head>

<script context="module">
    import { authCheck } from '../../utils/user';
    export async function preload(page, session) {
        // authCheck(session, this.redirect);
        const res = await this.fetch(`profileDetails/`);
        const userDetails = await res.json();
        return { userDetails };

    }
</script>  
<script>
    import Card from '../../components/Card.svelte';
    import TwoColumn from '../../components/TwoColumn.svelte';
    import ActionMini from '../../components/ActionMini.svelte';
    import AddClass from '../../components/AddClass.svelte'
    import PopUpForm from '../../components/PopUpForm.svelte'
    import Modal from '../../components/Modal.svelte'
    import Match from '../../components/Match.svelte'
    import Nav from '../../components/Nav.svelte'


    export let userDetails, mentorData;
    mentorData = userDetails.mentorData;

    let profileComplete = false;
    let user_type = 'Mentee';
    if (userDetails.user_type === 'MR') {
        user_type = 'Mentor'
    }
    if (userDetails.user_type==='MT' && userDetails.organization!=='' && userDetails.requirement!=='') {
        profileComplete = true;
    }
    if (userDetails.user_type ==='MR') {
        profileComplete = true;
    }
    let today = new Date()
    let curHr = today.getHours()
    let greeting = ''

    if (curHr < 12) {
        greeting = 'good morning'
    } else if (curHr < 18) {
        greeting = 'good afternoon'
    } else {
        greeting = 'good evening'
    }

    export let classList = []
    let i;
    for (i = 0; i < userDetails.classes.length; i ++){
        classList.push({
            name: userDetails.classes[i].title,
            uuid: userDetails.classes[i].uuid
        })
    }

    

    // console.log(userDetails)
    // console.log("ud above")
    // console.log(mentorData)
    // console.log(classList)
</script>

<Nav classList = {classList}/>



    <TwoColumn>
        <div slot="left">

                    <Card data="34" title="Number of mentees"  subtext="Mentee details" link="Some text" styleNumber="one"/>
                    <Card data="3" title="Current classes"  subtext="Manage classes" link="Some text" styleNumber="two"/>
                    <Card data="19" title="Active projects"  subtext="Review projects" link="Some text" styleNumber="three"/>
                <div class="action-mini_wrapper">
                    <ActionMini link="" icon="book-read-streamline" label="Add Resources" />
                    <Modal>
                        <PopUpForm icon="folder-add" label="Create Project" />
                    </Modal>
                    <ActionMini link="" icon="users" label="View Mentors" />
                    <Modal>
                        <AddClass icon="users" label="Create New Class" />
                    </Modal>
                </div>
        </div>
        <div slot="right">
            <div class="greet">
            <h1>{greeting}, {userDetails.first_name}</h1>
            <div class="badges">
                <div class="badge qualification">{userDetails.qualification}</div>
                <div class="badge user_type">{user_type}</div>
            </div>

            {#if profileComplete}
            <a class="button button-secondary" href="/profile/edit/">EDIT PROFILE</a>
            
            {:else}
            <div class="incomplete">
                <p class="sub">
                    Your profile seems to be incomplete, choose any of the two options below to continue...
                </p>

                <a class="button button-secondary" href="/mentoring/apply">APPLY FOR MENTOR</a>
                <a class="button button-secondary" href="/profile/complete/">COMPLETE PROFILE</a>
                </div>


            {/if}
        </div>
        {#if profileComplete}
            <div class="container">
            <h1>Your mentor recommendations</h1>
                {#each mentorData as mentor}
                        <div class="container2">
                        <Match first_name={mentor.first_name} last_name={mentor.last_name} time={mentor.duration} qualification={mentor.qualification} organization={mentor.organization} areas={mentor.requirements} styleNumber="two" ind=0/>
                        </div>
                {/each}
            </div>



        {/if}
		
        </div>
    </TwoColumn>
        
<!-- instant announcement -->