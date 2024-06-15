<script>
	let prompt = '';
	$: {
		console.log(prompt);
	}
	const fadeIn = 'rounded-br-2xl rounded-tr-2xl border-r-2 transition-all duration-300 ease-in';
	const unHide = 'opacity-100 transition-all duration-300 ease-in';
</script>

<div class="w-full flex flex-col">
	<div class={`flex justify-center gap-0`}>
		<input
			id="prompt"
			bind:value={prompt}
			type="text"
			class={`p-2 w-2/5 outline-none
            border-b-2 border-t-2 border-l-2
            rounded-bl-2xl rounded-tl-2xl
            ${prompt.length > 2 ? '' : fadeIn}`}
		/>
		<div
			class={`pr-1 flex items-center text-fluid-xs
                border-b-2 border-t-2 border-r-2
                rounded-br-2xl rounded-tr-2xl
                ${prompt.length > 2 ? unHide : 'opacity-0'}
              `}
		>
			<button
				on:click={() => {}}
				class={`px-[.75rem] py-[.35rem] border-[1px] border-black rounded-xl
              ${prompt.length > 2 ? unHide : 'opacity-0 hidden'}`}
			>
				Send
			</button>
		</div>
	</div>
</div>
