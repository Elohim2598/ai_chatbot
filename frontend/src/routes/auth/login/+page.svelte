<script lang="ts">
	import '../../../app.css';
	// State variables
	let showPassword: Boolean = false;

	// Buttons array with common styles
	let buttons = [
		{
			className: 'w-full block bg-black text-white border-2 border-black py-3 text-fluid-md mb-4',
			content: 'Login',
			buttonType: 'submit' as const
		},
		{
			className: 'w-full block bg-white border-2 border-black text-black py-3 text-fluid-md mb-4',
			content: 'Login with Google',
			buttonType: 'button' as const
		}
	];
</script>

<div class="relative min-h-screen flex flex-col items-center justify-center">
	<div
		class="w-full max-w-md space-y-8 relative min-h-screen flex flex-col items-center justify-center"
	>
		<!-- Header -->
		<div>
			<h1 class="mt-6 text-center text-5xl font-extrabold">Log In</h1>
			<h6 class="text-center mt-6 text-fluid-md">Lorem ipsum dolor sit amet adipiscing elit.</h6>
		</div>

		<!-- Form -->
		<form action="/login" method="POST" class="mt-8 space-y-6 flex flex-wrap w-full">
			<!-- Email input -->
			<div class="w-full px-3">
				<label for="email" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*EMAIL</label
				>
				<input
					id="email"
					type="text"
					class="block w-full bg-white text-gray-700 border py-3 px-3"
				/>
			</div>

			<!-- Password input -->
			<div class="w-full px-3">
				<label for="pw" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*PASSWORD</label
				>
				<input
					id="pw"
					type={showPassword ? 'text' : 'password'}
					class="block w-full bg-white text-gray-700 border py-3 px-3"
				/>
				<button
					type="button"
					class="text-fluid-sm text-gray-400 hover:text-gray-900"
					on:click={() => (showPassword = !showPassword)}
				>
					{#if showPassword}
						Hide Password
					{:else}
						Show Password
					{/if}
				</button>
			</div>

			<!-- Buttons -->
			<div class="w-11/12 mx-auto">
				{#each buttons as button}
					<button type={button.buttonType} class={button.className}>
						{button.content}
					</button>
				{/each}
				<a href="#" class="w-full flex justify-center"><u>Forgot your password?</u></a>
			</div>
		</form>
	</div>
</div>
