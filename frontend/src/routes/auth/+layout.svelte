<style>
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

<!-- Content -->
<div class="relative z-10 min-h-screen flex flex-col items-center justify-center px-4">
	<slot />
</div>
