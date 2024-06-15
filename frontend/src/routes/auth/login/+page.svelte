<script lang="ts">
	let showPassword: boolean = false;
</script>

<div class="w-full max-w-md space-y-8">
	<div>
		<h1 class="mt-6 text-center text-5xl font-extrabold">Log In</h1>
		<h6 class="text-center mt-6 text-fluid-md">Lorem ipsum dolor sit amet adipiscing elit.</h6>
	</div>
	<form action="/login" method="POST" class="mt-8 space-y-6 flex flex-wrap w-full">
		<div class="w-full px-3">
			<label class="block uppercase tracking-wide text-gray-700 text-sm font-bold" for="email">
				*EMAIL
			</label>
			<input class=" block w-full bg-white text-gray-700 border py-3 px-3" id="email" type="text" />
		</div>
		<div class="w-full px-3">
			<label class="block uppercase tracking-wide text-gray-700 text-sm font-bold" for="pw">
				*PASSWORD
			</label>
			<input
				class=" block w-full bg-white text-gray-700 border py-3 px-3"
				id="pw"
				type={showPassword ? 'text' : 'password'}
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
		<div class="w-[95%] mx-auto">
			<button
				type="submit"
				class="w-full block bg-black text-white border-2 border-black py-3 text-fluid-md mb-4"
			>
				Login
			</button>
			<button
				class="w-full block bg-white border-2 border-black text-black py-3 text-fluid-md mb-4"
			>
				<!-- Logo should go here -->
				Login with Google
			</button>
			<a href="#" class="w-full flex justify-center"><u>Forgot your password?</u></a>
		</div>
	</form>
</div>
