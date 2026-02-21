<script lang="ts">
	import { onMount } from 'svelte';
	import { gsap } from 'gsap';

	onMount(() => {
		gsap.set('.hero-icon', { scale: 0.4, opacity: 0 });
		gsap.set('.hero-title', { y: 30, opacity: 0 });
		gsap.set('.hero-sub', { y: 20, opacity: 0 });
		gsap.set('.hero-btn', { y: 20, opacity: 0 });

		gsap.to('.hero-icon',  { scale: 1, opacity: 1, duration: 0.8, delay: 0.1, ease: 'back.out(2)' });
		gsap.to('.hero-title', { y: 0, opacity: 1, duration: 0.7, delay: 0.35, ease: 'power3.out' });
		gsap.to('.hero-sub',   { y: 0, opacity: 1, duration: 0.6, delay: 0.5,  ease: 'power3.out' });
		gsap.to('.hero-btn',   { y: 0, opacity: 1, duration: 0.5, delay: 0.65, stagger: 0.1, ease: 'power3.out' });
	});
</script>

<style>
	.gradient-text {
		background: linear-gradient(135deg, #e8956a, #c87941, #f0a875);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}
</style>

<div class="text-center flex flex-col items-center gap-8 px-6 max-w-xl">
	<!-- Icon -->
	<div class="hero-icon relative">
		<div class="w-20 h-20 rounded-3xl bg-gradient-to-br from-[#c87941] to-[#a85e28] flex items-center justify-center shadow-2xl shadow-[#c87941]/40">
			<span class="text-white text-3xl">✦</span>
		</div>
		<div class="absolute inset-0 rounded-3xl bg-[#c87941]/30 blur-2xl -z-10 scale-110"></div>
	</div>

	<!-- Text -->
	<div class="space-y-4">
		<h1 class="hero-title gradient-text text-5xl font-bold tracking-tight">AI Chatbot</h1>
		<p class="hero-sub text-white/40 text-base leading-relaxed">
			A conversational AI assistant powered by Llama 3.3 70B.<br/>Fast, smart, and ready to help.
		</p>
	</div>

	<!-- Buttons -->
	<div class="flex gap-4 justify-center">
		<a
			href="/auth/login"
			class="hero-btn py-3 px-7 bg-gradient-to-br from-[#c87941] to-[#a85e28] text-white font-medium rounded-xl shadow-lg shadow-[#c87941]/30 hover:shadow-[#c87941]/50 hover:scale-105 transition-all duration-200"
		>
			Log In
		</a>
		<a
			href="/auth/register"
			class="hero-btn py-3 px-7 bg-white/[0.06] border border-white/[0.1] text-white/80 font-medium rounded-xl hover:bg-white/[0.1] hover:border-[#c87941]/30 transition-all duration-200"
		>
			Sign Up
		</a>
	</div>
</div>
