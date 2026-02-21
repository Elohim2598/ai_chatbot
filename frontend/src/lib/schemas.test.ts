import { describe, it, expect } from 'vitest';
import { loginSchema, registerSchema } from './schemas';

// ── loginSchema ───────────────────────────────────────────────────────────────

describe('loginSchema', () => {
	const valid = { email: 'user@example.com', password: 'secret123' };

	it('accepts valid credentials', async () => {
		await expect(loginSchema.validate(valid)).resolves.toBeDefined();
	});

	it('rejects an invalid email format', async () => {
		await expect(loginSchema.validate({ ...valid, email: 'not-an-email' })).rejects.toThrow(
			'Invalid email address'
		);
	});

	it('rejects an empty email', async () => {
		await expect(loginSchema.validate({ ...valid, email: '' })).rejects.toThrow(
			'Email is required'
		);
	});

	it('rejects a missing password', async () => {
		await expect(loginSchema.validate({ ...valid, password: '' })).rejects.toThrow(
			'Password is required'
		);
	});
});

// ── registerSchema ────────────────────────────────────────────────────────────

describe('registerSchema', () => {
	const valid = {
		name: 'John Doe',
		email: 'john@example.com',
		password: 'password123',
		confirmPassword: 'password123'
	};

	it('accepts valid registration data', async () => {
		await expect(registerSchema.validate(valid)).resolves.toBeDefined();
	});

	it('rejects an empty name', async () => {
		await expect(registerSchema.validate({ ...valid, name: '' })).rejects.toThrow(
			'Name is required'
		);
	});

	it('rejects an invalid email format', async () => {
		await expect(registerSchema.validate({ ...valid, email: 'bad-email' })).rejects.toThrow(
			'Invalid email address'
		);
	});

	it('rejects a password shorter than 8 characters', async () => {
		await expect(
			registerSchema.validate({ ...valid, password: 'short', confirmPassword: 'short' })
		).rejects.toThrow('Password must be at least 8 characters');
	});

	it('rejects mismatched passwords', async () => {
		await expect(
			registerSchema.validate({ ...valid, confirmPassword: 'different' })
		).rejects.toThrow('Passwords must match');
	});

	it('rejects a missing confirm password', async () => {
		// yup evaluates oneOf before required when the value is an empty string,
		// so the first error reported is the oneOf mismatch message.
		await expect(
			registerSchema.validate({ ...valid, confirmPassword: '' })
		).rejects.toThrow('Passwords must match');
	});
});
