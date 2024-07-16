<script lang="ts">
	export let isOpen = false;
	export let toggleDrawer: (side: 'left' | 'right') => void;
	export let side: 'left' | 'right' = 'left';
</script>

<!-- Another issue here, drawer is traveling all the way from the right side to the left side where the left drawer should be xd -->
<div
	class={`fixed inset-0 transition-transform ease-in-out duration-300 ${isOpen ? 'translate-x-0' : side === 'left' ? '-translate-x-full' : 'translate-x-full'}`}
>
	<div
		class={`bg-slate-950 h-full p-4 text-white w-4/5 lg:w-1/5 ${side === 'right' ? 'right-0' : 'left-0'}`}
	>
		<button on:click={() => toggleDrawer(side)} class="mb-4">Close</button>
		{#if side === 'left'}
			<slot name="left"></slot>
		{:else}
			<slot name="right"></slot>
		{/if}
	</div>
</div>
