<style>
	.gradient-text {
		background: linear-gradient(135deg, #e8956a, #c87941, #f0a875);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}
</style>

<div class="w-full max-w-sm text-center flex flex-col items-center gap-6">
	<div class="relative">
		<div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-[#c87941] to-[#a85e28] flex items-center justify-center shadow-xl shadow-[#c87941]/30">
			<span class="text-white text-2xl">✦</span>
		</div>
		<div class="absolute inset-0 rounded-2xl bg-[#c87941]/30 blur-xl -z-10 scale-110"></div>
	</div>

	<div class="bg-white/[0.04] border border-white/[0.08] rounded-2xl p-8 backdrop-blur-xl w-full flex flex-col items-center gap-4">
		<h1 class="gradient-text text-2xl font-bold">Authentication Error</h1>
		<p class="text-white/30 text-sm leading-relaxed">Something went wrong during sign in.<br/>Please try again.</p>
		<a
			href="/auth/login"
			class="mt-2 py-2.5 px-6 rounded-xl bg-gradient-to-br from-[#c87941] to-[#a85e28] text-white text-sm font-medium
				shadow-lg shadow-[#c87941]/20 hover:shadow-[#c87941]/40 hover:scale-[1.02] active:scale-[0.98] transition-all duration-200"
		>
			Back to Login
		</a>
	</div>
</div>
