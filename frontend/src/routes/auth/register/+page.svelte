<script lang="ts">
	// State variables
	let showPassword: Boolean = false;
	let password: string = '';
	let confirmPassword: string = '';
	let passwordsMatch: Boolean = true;
	let passwordValid: Boolean = false;

	function handleSubmit() {
		if (password !== confirmPassword) {
			passwordsMatch = false;
		} else {
			// Submit the form
			console.log('Form submitted');
		}
	}

	function handlePasswordInput(event: Event & { currentTarget: EventTarget & HTMLInputElement }) {
		password = (event.target as HTMLInputElement).value;
		checkPasswordsMatch();
	}

	function handleConfirmPasswordInput(
		event: Event & { currentTarget: EventTarget & HTMLInputElement }
	) {
		confirmPassword = (event.target as HTMLInputElement).value;
		checkPasswordsMatch();
		checkPasswordValidity();
	}

	function checkPasswordValidity() {
		if (password.length >= 8) {
			passwordValid = true;
		} else {
			passwordValid = false;
		}
	}

	function checkPasswordsMatch() {
		if (password !== confirmPassword) {
			passwordsMatch = false;
		} else {
			passwordsMatch = true;
		}
	}
</script>

<div class="relative min-h-screen flex flex-col items-center justify-center">
	<div
		class="w-full max-w-md space-y-8 relative min-h-screen flex flex-col items-center justify-center"
	>
		<!-- Header -->
		<div>
			<h1 class="mt-6 text-center text-5xl font-extrabold">Sign up</h1>
			<h6 class="text-center mt-6 text-fluid-md">Lorem ipsum dolor sit amet adipiscing elit.</h6>
		</div>

		<!-- Form -->
		<form
			action="/signup"
			method="POST"
			class="mt-8 space-y-2 flex flex-wrap w-full"
			on:submit={handleSubmit}
		>
			<!-- Name input -->
			<div class="w-full px-3">
				<label for="name" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*FULL NAME</label
				>
				<input id="name" type="text" class="block w-full bg-white text-gray-700 border py-3 px-3" />
			</div>

			<!-- Email input -->
			<div class="w-full px-3">
				<label for="email" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*EMAIL</label
				>
				<input
					id="email"
					type="email"
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
					type="password"
					class="block w-full bg-white text-gray-700 border py-3 px-3"
					on:input={handlePasswordInput}
				/>
			</div>
			{#if !passwordValid}
				<p class="text-red-500 text-sm px-4">Password must be at least 8 characters long</p>
			{/if}
			<!-- Confirm Password input -->
			<div class="w-full px-3">
				<label for="confirmPw" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*CONFIRM PASSWORD</label
				>
				<input
					id="confirmPw"
					type="password"
					class="block w-full bg-white text-gray-700 border py-3 px-3"
					on:input={handleConfirmPasswordInput}
				/>
			</div>
			{#if !passwordsMatch}
				<p class="text-red-500 text-sm px-4">Passwords do not match</p>
			{/if}
			<!-- Button -->
			<div class="w-11/12 mx-auto mt-6">
				<button
					type="submit"
					class="w-full block bg-black text-white border-2 border-black py-3 text-fluid-md mb-4"
				>
					Sign up
				</button>
				<a href="/auth/login" class="w-full flex justify-center"
					><u>Already have an account? Login</u></a
				>
			</div>
		</form>
	</div>
</div>
