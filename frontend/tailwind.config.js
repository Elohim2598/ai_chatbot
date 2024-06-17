/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			fontSize: {
				'fluid-xs': 'var(--step--2)',
				'fluid-sm': 'var(--step--1)',
				'fluid-md': 'var(--step-0)',
				'fluid-lg': 'var(--step-1)',
				'fluid-xl': 'var(--step-2)',
				'fluid-2xl': 'var(--step-3)',
				'fluid-3xl': 'var(--step-4)'
			}
		}
	},
	plugins: []
};
