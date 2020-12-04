<script>
  import { getContext } from 'svelte';
	import { fly } from 'svelte/transition';
	
	import Dialog from './Dialog.svelte';
	import CloseButton from './CloseButton.svelte';

  const { open } = getContext('simple-modal');
	
	let opening = false;
	let opened = false;
	let closing = false;
	let closed = false;

  
	let project_name;
	let project_text;
	let status = 0;
	
	const onCancel = (text) => {
		name = '';
		status = -1;
	}
	
	const onOkay = (name, text) => {
		project_name = name;
		project_text = text;
		console.log(text)
		status = 1;
	}

  const showDialog = () => {
		open(
			Dialog,
			{
				message: "Enter Project Details",
				hasForm: true,
				onCancel,
				onOkay
			},
			{
				closeButton: true,
    			closeOnEsc: false,
    			closeOnOuterClick: false,
			}
	  );
	};
</script>

<section>
	<button on:click={showDialog}>Add New Project</button>

	<!-- {#if status === 1}
		<p>Hi {project_name}! 👋</p>
	{:else if status === -1}
		<p><em>Dialog was canceled</em></p>
	{/if}

	<div id="state">
		{#if opening}
			<p>opening modal...</p>
		{:else if opened}
			<p>opened modal!</p>
		{:else if closing}
			<p>closing modal...</p>
		{:else if closed}
			<p>closed modal!</p>
		{/if}
	</div> -->
</section>

<style>
	section {
		padding-top: 0.5em;
	}
	
	#state {
		position: absolute;
		top: 0;
		right: 0;
		opacity: 0.33;
		font-size: 0.8em;
	}
</style>