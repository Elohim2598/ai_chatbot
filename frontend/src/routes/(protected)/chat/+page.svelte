<script lang="ts">
	import Drawer from '../../../components/ui/drawer/Drawer.svelte';

	type Message = {
		text: string;
		sender: 'user' | 'ai';
	};

	let messages: Message[] = [];
	let newMessage = '';
	let isOpenLeft = false;
	let isOpenRight = false;

	function sendMessage() {
		if (newMessage.trim() !== '') {
			messages = [...messages, { text: newMessage, sender: 'user' }];
			newMessage = '';

			const textarea = document.querySelector('textarea') as HTMLTextAreaElement;
			if (textarea) {
				textarea.style.height = 'auto';
			}

			setTimeout(() => {
				messages = [...messages, { text: 'This is an AI response.', sender: 'ai' }];
			}, 1000);
		}
	}

	function autoGrow(event: Event) {
		const target = event.target as HTMLTextAreaElement;
		target.style.height = 'auto';
		const maxHeight = 100;
		target.style.height = Math.min(target.scrollHeight, maxHeight) + 'px';
		target.style.overflowY = target.scrollHeight > maxHeight ? 'auto' : 'hidden';
	}

	function toggleDrawer(side: 'left' | 'right') {
		if (side === 'left') {
			isOpenLeft = !isOpenLeft;
		} else {
			isOpenRight = !isOpenRight;
		}
	}
</script>

<div class="flex h-screen p-4 bg-gray-800 m-auto">
	<Drawer isOpen={isOpenLeft} {toggleDrawer} side="left">
		<div slot="left">
			<p>Left side drawer</p>
		</div>
	</Drawer>
	<div class="flex flex-col flex-1 transition-all duration-300">
		<div class="flex flex-row justify-between items-center">
			<button on:click={() => toggleDrawer('left')} class="mb-4 mr-auto text-white">
				{isOpenLeft ? '' : 'Chat History'}
			</button>
			<button on:click={() => toggleDrawer('right')} class="mb-4 ml-auto text-white">
				{isOpenRight ? '' : 'Profile'}
			</button>
		</div>
		<div class="flex-1 overflow-y-auto mb-4 space-y-2">
			{#each messages as message}
				<!-- Have one issue here, when typing a very long message it overflows and breaks it-->
				<div
					class={`max-w-xs p-2 text-white break-words max-w-full ${message.sender === 'user' ? 'bg-gray-700 justify-right w-2/3 ml-auto' : 'self-start mr-auto'}`}
				>
					{message.text}
				</div>
			{/each}
		</div>

		<div class="flex">
			<textarea
				bind:value={newMessage}
				class="flex-1 p-2 border border-gray-300 focus:outline-none focus:ring-0 focus:border-gray-300 focus:rounded-none active:ring-0 active:border-gray-300 active:rounded-none resize-none overflow-hidden"
				placeholder="Type a message..."
				on:keydown={(e) => {
					if (e.key === 'Enter' && !e.shiftKey) {
						e.preventDefault();
						sendMessage();
					}
				}}
				on:input={autoGrow}
				rows="1"
			></textarea>
			<button on:click={sendMessage} class="ml-2 p-2 bg-black text-white">Send</button>
		</div>
	</div>
	<Drawer isOpen={isOpenRight} {toggleDrawer} side="right">
		<div slot="right">
			<p>Right side drawer</p>
		</div>
	</Drawer>
</div>
