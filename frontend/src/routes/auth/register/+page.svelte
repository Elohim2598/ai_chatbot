<script lang="ts">
	import { onMount } from 'svelte';
	import { gsap } from 'gsap';
	import { createForm } from 'svelte-forms-lib';
	import { registerSchema } from '$lib/schemas';

	let formEl: HTMLFormElement;

	const { form, errors, handleChange, handleSubmit } = createForm({
		initialValues: {
			name: '',
			email: '',
			password: '',
			confirmPassword: ''
		},
		validationSchema: registerSchema,
		onSubmit: () => formEl.submit()
	});

	onMount(() => {
		gsap.set('.auth-card', { y: 32, opacity: 0 });
		gsap.to('.auth-card', { y: 0, opacity: 1, duration: 0.7, delay: 0.1, ease: 'power3.out' });
	});
</script>

<style>
	.gradient-text {
		background: linear-gradient(135deg, #e8956a, #c87941, #f0a875);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}
	input:-webkit-autofill,
	input:-webkit-autofill:hover,
	input:-webkit-autofill:focus {
		-webkit-box-shadow: 0 0 0px 1000px rgba(255,255,255,0.04) inset;
		-webkit-text-fill-color: rgba(255,255,255,0.9);
		caret-color: rgba(255,255,255,0.9);
	}
</style>

<div class="auth-card w-full max-w-sm">
	<!-- Logo -->
	<div class="flex flex-col items-center gap-4 mb-8">
		<div class="relative">
			<div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-[#c87941] to-[#a85e28] flex items-center justify-center shadow-xl shadow-[#c87941]/30">
				<span class="text-white text-2xl">✦</span>
			</div>
			<div class="absolute inset-0 rounded-2xl bg-[#c87941]/30 blur-xl -z-10 scale-110"></div>
		</div>
		<div class="text-center">
			<h1 class="gradient-text text-3xl font-bold tracking-tight">Create account</h1>
			<p class="text-white/30 text-sm mt-1">Join AI Chatbot today</p>
		</div>
	</div>

	<!-- Card -->
	<div class="bg-white/[0.04] border border-white/[0.08] rounded-2xl p-8 backdrop-blur-xl">
		<form bind:this={formEl} action="?/signup" method="POST" on:submit={handleSubmit} class="flex flex-col gap-5">
			<!-- Name -->
			<div class="flex flex-col gap-1.5">
				<label for="name" class="text-white/50 text-xs uppercase tracking-widest font-medium">Full name</label>
				<input
					id="name"
					name="name"
					type="text"
					placeholder="John Doe"
					class="w-full bg-white/[0.04] border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white/90 placeholder-white/20 outline-none
						focus:border-[#c87941]/40 focus:bg-white/[0.06] transition-all duration-200"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.name}
				/>
				{#if $errors.name}
					<p class="text-red-400/80 text-xs">{$errors.name}</p>
				{/if}
			</div>

			<!-- Email -->
			<div class="flex flex-col gap-1.5">
				<label for="email" class="text-white/50 text-xs uppercase tracking-widest font-medium">Email</label>
				<input
					id="email"
					name="email"
					type="email"
					placeholder="you@example.com"
					class="w-full bg-white/[0.04] border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white/90 placeholder-white/20 outline-none
						focus:border-[#c87941]/40 focus:bg-white/[0.06] transition-all duration-200"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.email}
				/>
				{#if $errors.email}
					<p class="text-red-400/80 text-xs">{$errors.email}</p>
				{/if}
			</div>

			<!-- Password -->
			<div class="flex flex-col gap-1.5">
				<label for="password" class="text-white/50 text-xs uppercase tracking-widest font-medium">Password</label>
				<input
					id="password"
					name="password"
					type="password"
					placeholder="Min. 8 characters"
					class="w-full bg-white/[0.04] border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white/90 placeholder-white/20 outline-none
						focus:border-[#c87941]/40 focus:bg-white/[0.06] transition-all duration-200"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.password}
				/>
				{#if $errors.password}
					<p class="text-red-400/80 text-xs">{$errors.password}</p>
				{/if}
			</div>

			<!-- Confirm Password -->
			<div class="flex flex-col gap-1.5">
				<label for="confirmPassword" class="text-white/50 text-xs uppercase tracking-widest font-medium">Confirm password</label>
				<input
					id="confirmPassword"
					name="confirmPassword"
					type="password"
					placeholder="••••••••"
					class="w-full bg-white/[0.04] border border-white/[0.08] rounded-xl px-4 py-3 text-sm text-white/90 placeholder-white/20 outline-none
						focus:border-[#c87941]/40 focus:bg-white/[0.06] transition-all duration-200"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.confirmPassword}
				/>
				{#if $errors.confirmPassword}
					<p class="text-red-400/80 text-xs">{$errors.confirmPassword}</p>
				{/if}
			</div>

			<!-- Submit -->
			<button
				type="submit"
				class="w-full py-3 rounded-xl bg-gradient-to-br from-[#c87941] to-[#a85e28] text-white text-sm font-medium
					shadow-lg shadow-[#c87941]/20 hover:shadow-[#c87941]/40 hover:scale-[1.02] active:scale-[0.98] transition-all duration-200 mt-1"
			>
				Create account
			</button>
		</form>
	</div>

	<!-- Footer links -->
	<div class="flex flex-col items-center gap-2 mt-5">
		<a href="/auth/login" class="text-white/30 text-xs hover:text-white/50 transition-colors">
			Already have an account? <span class="text-[#e8956a]/70 hover:text-[#e8956a]">Log in</span>
		</a>
	</div>
</div>
