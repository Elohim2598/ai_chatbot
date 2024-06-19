<script>
	import { teamMembers } from './constants';
</script>

<div class="relative min-h-screen w-full flex flex-col items-center justify-center">
	<ul
		class="flex flex-col justify-evenly gap-5
            sm:flex-row sm:w-2/3
            md:flex-row md:w-4/5"
	>
		{#each teamMembers as teamMember}
			<li class="grid place-items-center">
				<img
					src={teamMember.image}
					alt="Team member"
					width={teamMember.width}
					class={teamMember.className}
				/>
				<span>{teamMember.name}</span>
			</li>
		{/each}
	</ul>
</div>
