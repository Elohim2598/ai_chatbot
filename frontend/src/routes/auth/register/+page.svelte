<script lang="ts">
	import { createForm } from 'svelte-forms-lib';
	import * as yup from 'yup';

	const { form, errors, handleChange, handleSubmit } = createForm({
		initialValues: {
			name: '',
			email: '',
			password: '',
			confirmPassword: ''
		},
		validationSchema: yup.object().shape({
			name: yup.string().required('Name is required'),
			email: yup.string().email('Invalid email address').required('Email is required'),
			password: yup
				.string()
				.min(8, 'Password must be at least 8 characters')
				.required('Password is required'),
			confirmPassword: yup
				.string()
				.oneOf([yup.ref('password')], 'Passwords must match')
				.required('Confirm password is required')
		}),
		onSubmit: (values) => {
			alert(JSON.stringify(values));
		}
	});
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
		<form action="?/signup" method="POST" class="mt-8 space-y-2 flex flex-wrap w-full">
			<!-- Name input -->
			<div class="w-full px-3">
				<label for="name" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*FULL NAME</label
				>
				<input
					id="name"
					name="name"
					type="text"
					class="block w-full bg-white text-gray-700 border py-3 px-3"
					placeholder="John Doe"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.name}
				/>
			</div>
			{#if $errors.name}
				<p class="text-red-500 text-sm px-4">{$errors.name}</p>
			{/if}
			<!-- Email input -->
			<div class="w-full px-3">
				<label for="email" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*EMAIL</label
				>
				<input
					id="email"
					name="email"
					type="email"
					class="block w-full bg-white text-gray-700 border py-3 px-3"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.email}
				/>
			</div>
			{#if $errors.email}
				<p class="text-red-500 text-sm px-4">{$errors.email}</p>
			{/if}
			<!-- Password input -->
			<div class="w-full px-3">
				<label for="pw" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*PASSWORD</label
				>
				<input
					id="password"
					name="password"
					type="password"
					class="block w-full bg-white text-gray-700 border py-3 px-3"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.password}
				/>
			</div>
			{#if $errors.password}
				<p class="text-red-500 text-sm px-4">{$errors.password}</p>
			{/if}
			<!-- Confirm Password input -->
			<div class="w-full px-3">
				<label for="confirmPw" class="block uppercase tracking-wide text-gray-700 text-sm font-bold"
					>*CONFIRM PASSWORD</label
				>
				<input
					id="confirmPassword"
					name="confirmPassword"
					type="password"
					class="block w-full bg-white text-gray-700 border py-3 px-3"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.confirmPassword}
				/>
			</div>
			{#if $errors.confirmPassword}
				<p class="text-red-500 text-sm px-4">{$errors.confirmPassword}</p>
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
