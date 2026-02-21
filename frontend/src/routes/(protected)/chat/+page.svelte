<script lang="ts">
	import { tick, onMount } from 'svelte';
	import { gsap } from 'gsap';

	export let data;
	$: ({ session } = data);

	type Message = {
		id: number;
		role: 'user' | 'model';
		content: string;
	};

	let messages: Message[] = [];
	let input = '';
	let loading = false;
	let messagesEnd: HTMLElement;
	let textarea: HTMLTextAreaElement;

	function autoResize() {
		if (!textarea) return;
		textarea.style.height = 'auto';
		const maxHeight = 160;
		const newHeight = Math.min(textarea.scrollHeight, maxHeight);
		textarea.style.height = newHeight + 'px';
		textarea.style.overflowY = textarea.scrollHeight > maxHeight ? 'auto' : 'hidden';
	}

	function resetHeight() {
		if (textarea) textarea.style.height = 'auto';
	}

	// Page entrance animations
	onMount(() => {
		gsap.set('header', { y: -80, opacity: 0 });
		gsap.to('header', { y: 0, opacity: 1, duration: 0.7, ease: 'power4.out' });
		gsap.set('footer', { y: 80, opacity: 0 });
		gsap.to('footer', { y: 0, opacity: 1, duration: 0.7, ease: 'power4.out' });
	});

	// Actions for empty state elements
	function emptyIcon(node: HTMLElement) {
		gsap.set(node, { scale: 0.4, opacity: 0 });
		gsap.to(node, { scale: 1, opacity: 1, duration: 0.8, delay: 0.25, ease: 'back.out(2)' });
	}
	function emptyHeading(node: HTMLElement) {
		gsap.set(node, { y: 24, opacity: 0 });
		gsap.to(node, { y: 0, opacity: 1, duration: 0.6, delay: 0.5, ease: 'power3.out' });
	}
	function emptySub(node: HTMLElement) {
		gsap.set(node, { y: 16, opacity: 0 });
		gsap.to(node, { y: 0, opacity: 1, duration: 0.5, delay: 0.65, ease: 'power3.out' });
	}
	function chipIn(node: HTMLElement, i: number) {
		gsap.set(node, { y: 20, opacity: 0 });
		gsap.to(node, { y: 0, opacity: 1, duration: 0.45, delay: 0.8 + i * 0.08, ease: 'power3.out' });
	}

	// Svelte action: animate each message in as it mounts
	function messageIn(node: HTMLElement, role: 'user' | 'model') {
		gsap.from(node, {
			x: role === 'user' ? 60 : -30,
			opacity: 0,
			duration: 0.45,
			ease: 'power3.out'
		});
	}

	// Svelte action: animate typing indicator in
	function typingIn(node: HTMLElement) {
		gsap.from(node, {
			x: -20,
			opacity: 0,
			duration: 0.35,
			ease: 'power3.out'
		});
	}

	// Send button click burst
	function onSendClick(e: MouseEvent) {
		const btn = e.currentTarget as HTMLElement;
		if (!input.trim() || loading) return;
		gsap.timeline()
			.to(btn, { scale: 0.82, duration: 0.1, ease: 'power2.in' })
			.to(btn, { scale: 1, duration: 0.35, ease: 'elastic.out(1.4, 0.5)' });
		sendMessage();
	}

	async function scrollToBottom() {
		await tick();
		messagesEnd?.scrollIntoView({ behavior: 'smooth' });
	}

	async function sendMessage() {
		const text = input.trim();
		if (!text || loading) return;

		input = '';
		resetHeight();
		messages = [...messages, { id: Date.now(), role: 'user', content: text }];
		loading = true;
		await scrollToBottom();

		const history = messages.slice(0, -1).map((m) => ({
			role: m.role,
			parts: [m.content]
		}));

		try {
			const res = await fetch('http://127.0.0.1:5000/api/v1/chat', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${session?.access_token}`
				},
				body: JSON.stringify({ message: text, history })
			});

			const json = await res.json();
			const reply = json.reply ?? json.error ?? 'No response received.';
			messages = [...messages, { id: Date.now() + 1, role: 'model', content: reply }];
		} catch (e) {
			messages = [
				...messages,
				{ id: Date.now() + 1, role: 'model', content: `Error: ${e}` }
			];
		} finally {
			loading = false;
			await scrollToBottom();
		}
	}

	function handleKeydown(e: KeyboardEvent) {
		if (e.key === 'Enter' && !e.shiftKey) {
			e.preventDefault();
			sendMessage();
		}
	}
</script>

<style>
	.scrollbar-hide::-webkit-scrollbar { display: none; }
	.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }

	textarea::-webkit-scrollbar { width: 4px; }
	textarea::-webkit-scrollbar-track { background: transparent; }
	textarea::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); border-radius: 9999px; }
	textarea::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.25); }

	@keyframes float-slow {
		0%, 100% { transform: translateY(0px) scale(1); }
		50% { transform: translateY(-40px) scale(1.05); }
	}
	@keyframes float-med {
		0%, 100% { transform: translateY(0px) scale(1); }
		50% { transform: translateY(30px) scale(0.97); }
	}
	.orb-1 { animation: float-slow 12s ease-in-out infinite; }
	.orb-2 { animation: float-med 9s ease-in-out infinite; }
	.orb-3 { animation: float-slow 15s ease-in-out infinite reverse; }
	.orb-4 { animation: float-med 11s ease-in-out infinite reverse; }

	.gradient-text {
		background: linear-gradient(135deg, #e8956a, #c87941, #f0a875);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}
</style>

<!-- Background -->
<div class="fixed inset-0 bg-[#0d0905]">
	<div class="orb-1 absolute -top-32 -left-32 w-[700px] h-[700px] rounded-full blur-[160px]" style="background: rgba(180,90,30,0.18);"></div>
	<div class="orb-2 absolute top-1/3 -right-48 w-[650px] h-[650px] rounded-full blur-[150px]" style="background: rgba(200,121,65,0.12);"></div>
	<div class="orb-3 absolute -bottom-32 left-1/4 w-[600px] h-[600px] rounded-full blur-[140px]" style="background: rgba(160,70,20,0.14);"></div>
	<div class="orb-4 absolute top-2/3 -left-20 w-[400px] h-[400px] rounded-full blur-[120px]" style="background: rgba(220,140,60,0.09);"></div>
	<div class="absolute inset-0 opacity-[0.03]"
		style="background-image: linear-gradient(rgba(255,255,255,0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.5) 1px, transparent 1px); background-size: 60px 60px;">
	</div>
</div>

<!-- App shell -->
<div class="relative z-10 flex flex-col h-screen">

	<!-- Header -->
	<header class="w-full border-b border-white/[0.05] bg-black/20 backdrop-blur-2xl">
		<div class="max-w-[1400px] mx-auto px-10 py-4 flex items-center justify-between">
			<div class="flex items-center gap-3">
				<div class="relative w-9 h-9 rounded-xl bg-gradient-to-br from-[#c87941] to-[#a85e28] flex items-center justify-center shadow-lg shadow-[#c87941]/30">
					<span class="text-white text-base">✦</span>
					<div class="absolute inset-0 rounded-xl bg-gradient-to-br from-[#e8956a] to-[#a85e28] blur-md opacity-60 -z-10"></div>
				</div>
				<span class="gradient-text font-bold text-base tracking-tight">AI Chatbot</span>
			</div>
			<div class="flex items-center gap-3">
				<div class="flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.07]">
					<span class="w-1.5 h-1.5 rounded-full bg-emerald-400 shadow shadow-emerald-400/80 animate-pulse"></span>
					<span class="text-white/40 text-xs tracking-widest uppercase font-medium">Llama 3.3 · 70B</span>
				</div>
				<form method="POST" action="/auth/logout">
					<button type="submit" class="px-3 py-1.5 rounded-full bg-white/[0.04] border border-white/[0.07] text-white/40 text-xs hover:bg-white/[0.08] hover:text-white/60 transition-all duration-200">
						Log out
					</button>
				</form>
			</div>
		</div>
	</header>

	<!-- Messages -->
	<main class="flex-1 overflow-y-auto scrollbar-hide">
		<div class="max-w-[1400px] mx-auto px-10">

			{#if messages.length === 0}
				<div class="flex flex-col items-center justify-center min-h-full py-32 gap-6 text-center select-none">
					<div use:emptyIcon class="relative">
						<div class="w-24 h-24 rounded-3xl bg-gradient-to-br from-[#c87941] to-[#a85e28] flex items-center justify-center shadow-2xl shadow-[#c87941]/40">
							<span class="text-white text-4xl">✦</span>
						</div>
						<div class="absolute inset-0 rounded-3xl bg-[#c87941]/30 blur-2xl -z-10 scale-110"></div>
					</div>
					<div class="space-y-3 max-w-md">
						<h2 use:emptyHeading class="gradient-text text-3xl font-bold tracking-tight">How can I help you today?</h2>
						<p use:emptySub class="text-white/30 text-sm leading-relaxed">Ask me anything. I'm powered by Llama 3.3 70B and ready to assist.</p>
					</div>
					<div class="flex flex-wrap gap-2 justify-center mt-2">
						{#each ['Explain a concept', 'Write some code', 'Brainstorm ideas', 'Summarize text'] as suggestion, i}
							<button
								use:chipIn={i}
								class="px-4 py-2 rounded-full bg-white/[0.05] border border-white/[0.08] text-white/50 text-xs hover:bg-white/[0.08] hover:text-white/70 hover:border-[#c87941]/30 transition-all duration-200"
								on:click={() => { input = suggestion; }}
							>
								{suggestion}
							</button>
						{/each}
					</div>
				</div>
			{/if}

			{#if messages.length > 0}
				<div class="py-8 space-y-8">
					{#each messages as message (message.id)}
						{#if message.role === 'user'}
							<div class="flex justify-end" use:messageIn={'user'}>
								<div class="max-w-[55%] px-5 py-3.5 rounded-2xl rounded-br-sm bg-gradient-to-br from-[#c87941]/80 to-[#a85e28]/80 border border-[#c87941]/30 text-white text-sm leading-relaxed whitespace-pre-wrap backdrop-blur-sm shadow-lg shadow-[#c87941]/10">
									{message.content}
								</div>
							</div>
						{:else}
							<div class="flex gap-5 items-start" use:messageIn={'model'}>
								<div class="relative flex-shrink-0 mt-0.5">
									<div class="w-8 h-8 rounded-xl bg-gradient-to-br from-[#c87941] to-[#a85e28] flex items-center justify-center shadow-lg shadow-[#c87941]/30">
										<span class="text-white text-sm">✦</span>
									</div>
									<div class="absolute inset-0 rounded-xl bg-[#c87941]/20 blur-lg -z-10"></div>
								</div>
								<div class="flex-1 min-w-0 text-white/80 text-sm leading-7 whitespace-pre-wrap pt-1">
									{message.content}
								</div>
							</div>
						{/if}
					{/each}

					{#if loading}
						<div class="flex gap-5 items-start" use:typingIn>
							<div class="relative flex-shrink-0">
								<div class="w-8 h-8 rounded-xl bg-gradient-to-br from-[#c87941] to-[#a85e28] flex items-center justify-center shadow-lg shadow-[#c87941]/30">
									<span class="text-white text-sm">✦</span>
								</div>
								<div class="absolute inset-0 rounded-xl bg-[#c87941]/20 blur-lg -z-10"></div>
							</div>
							<div class="flex gap-1.5 items-center pt-3">
								<span class="w-1.5 h-1.5 bg-[#e8956a] rounded-full animate-bounce [animation-delay:0ms]"></span>
								<span class="w-1.5 h-1.5 bg-[#e8956a] rounded-full animate-bounce [animation-delay:150ms]"></span>
								<span class="w-1.5 h-1.5 bg-[#e8956a] rounded-full animate-bounce [animation-delay:300ms]"></span>
							</div>
						</div>
					{/if}

					<div bind:this={messagesEnd}></div>
				</div>
			{/if}

		</div>
	</main>

	<!-- Input -->
	<footer class="w-full bg-black/20 backdrop-blur-2xl border-t border-white/[0.05]">
		<div class="max-w-[1400px] mx-auto px-10 py-5">
			<div class="flex items-end gap-4 bg-white/[0.04] border border-white/[0.08] rounded-2xl px-5 py-4
				focus-within:border-[#c87941]/30 focus-within:bg-white/[0.06] transition-all duration-300">
				<textarea
					bind:this={textarea}
					bind:value={input}
					on:input={autoResize}
					on:keydown={handleKeydown}
					placeholder="Ask anything..."
					rows="1"
					class="flex-1 resize-none bg-transparent text-sm text-white/90 placeholder-white/20 outline-none leading-relaxed overflow-y-auto transition-[height] duration-100 scrollbar-thin scrollbar-thumb-white/20 scrollbar-track-transparent"
				></textarea>
				<button
					on:click={onSendClick}
					disabled={!input.trim() || loading}
					class="flex-shrink-0 w-9 h-9 rounded-xl flex items-center justify-center transition-colors duration-200
						{input.trim() && !loading
							? 'bg-gradient-to-br from-[#c87941] to-[#a85e28] text-white shadow-lg shadow-[#c87941]/40'
							: 'bg-white/[0.04] text-white/20 cursor-not-allowed'}"
				>
					<svg xmlns="http://www.w3.org/2000/svg" class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="currentColor">
						<path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
					</svg>
				</button>
			</div>
			<p class="text-center text-white/[0.12] text-xs mt-3 tracking-wide">Enter to send · Shift+Enter for new line</p>
		</div>
	</footer>

</div>
