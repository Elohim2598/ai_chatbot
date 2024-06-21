<script lang="ts">
	export let label: string;
	export let type: 'button' | 'reset' | 'submit' = 'button';
	export let disabled: boolean = false;
	export let onClick: (event: MouseEvent) => void;
	export let variant: string = 'primary';
	export let size: string = 'medium';

	function getClass(variant: string, size: string): string {
		return `${variant} ${size}`;
	}
</script>

<button {type} {disabled} on:click={onClick} class={getClass(variant, size)}>
	{label}
</button>

<style>
	.primary {
		@apply bg-black text-white py-2 px-4;
	}

	.secondary {
		@apply bg-gray-600 text-white py-2 px-4;
	}

	.ghost {
		@apply bg-transparent border border-gray-600 text-gray-600 py-2 px-4;
	}

	.link {
		@apply text-blue-600 underline py-2 px-4;
	}

	.danger {
		@apply bg-red-600 text-white py-2 px-4;
	}

	.small {
		@apply py-1 px-2;
	}

	.medium {
		@apply py-2 px-4;
	}

	.large {
		@apply py-3 px-6;
	}
</style>
