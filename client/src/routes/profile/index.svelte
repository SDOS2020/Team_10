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

    export let userDetails;
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

    

    console.log(userDetails)
</script>




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
        <div ref = "childClass" slot="right">
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
    </TwoColumn>
        
<!-- instant announcement -->