<script>
	import { slide } from 'svelte/transition';
	let visible = true;
	export let sections = [
		{
			id: 1,
			title: "Section 1",
			content: "This is some test content",
			active: false,
		},
		{
			id: 2,
			title: "Section 2",
			content: "Welcome to section 2 test content",
			active: false,
		},
		{
			id: 3,
			title: "Section 3",
			content: "Looks like you have found what is hidden behind door number 3",
			active: false,
		}
	]
	
	const expand = (section) => {
		sections = sections.map(s => {
// 			s.active = false
			
			if (s.id === section.id) {
				if (s.active == false) s.active = true
				else s.active = false
			}
			return s
		})
	}
</script>

<style>
	 /* Style the buttons that are used to open and close the accordion panel */
.accordion {
  background-color: #eee;
  color: #444;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  text-align: left;
  border: none;
  outline: none;
  transition: 1s;
}

/* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
.active, .accordion:hover {
  background-color: #ccc;
}

/* Style the accordion panel. Note: hidden by default */
.panel {
  padding: 0 18px;
  background-color: white;
  display: none;
  overflow: hidden;
} 
	

</style>

{#each sections as section}
	<button class="accordion" on:click={() => expand(section) }>{section.title}</button>

	{#if section.active}
		<div class="slider" transition:slide>
			<p>{section.content}</p>
		</div>
	{/if}
{/each}