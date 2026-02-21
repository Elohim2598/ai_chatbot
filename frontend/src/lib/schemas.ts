import * as yup from 'yup';

export const loginSchema = yup.object().shape({
	email: yup.string().email('Invalid email address').required('Email is required'),
	password: yup.string().required('Password is required')
});

export const registerSchema = yup.object().shape({
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
});
