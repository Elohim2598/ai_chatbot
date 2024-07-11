import { redirect } from '@sveltejs/kit';

import type { Actions } from './$types';

export const actions: Actions = {
	signup: async ({ request, locals: { supabase } }) => {
		const formData = await request.formData();
		const name = formData.get('name') as string;
		const email = formData.get('email') as string;
		const password = formData.get('password') as string;

		const { error } = await supabase.auth.signUp({
			email,
			password,
			options: {
				data: {
					name: name
				}
			}
		});
		if (error) {
			console.error(error);
			return redirect(303, '/auth/error');
		} else {
			return redirect(303, '/chat');
		}
	}
};
