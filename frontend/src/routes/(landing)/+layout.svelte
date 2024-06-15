<script>
	import '../../app.css';
	import Footing from '../../components/ui/footing/Footing.svelte';
	import Heading from '../../components/ui/heading/Heading.svelte';
</script>

<div class="relative min-h-screen flex flex-col items-center justify-center">
	<Heading />
	<slot />
	<Footing />
</div>
