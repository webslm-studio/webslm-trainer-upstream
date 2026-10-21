# WebSLM Trainer

**Fine-tune a small language model on your own computer.** WebSLM Trainer is a desktop-first fork of [Unsloth](https://github.com/unslothai/unsloth), developed by [WebSLM Studio](https://github.com/webslm-studio). It puts smaller training models first while keeping larger language models available.

This repository is an early development fork, not a packaged WebSLM Trainer release. The first changes provide WebSLM naming in the desktop interface and an SLM-first order in the training model picker. Training still uses Unsloth's existing engine and hardware support.

## Development

The desktop interface lives in `studio/frontend/` and the native shell in `studio/src-tauri/`. The training backend lives in `studio/backend/`; the core engine retains the `unsloth` Python namespace for compatibility. The `webslm_trainer` Python import and command are aliases for this fork, not a separate training engine.

For a frontend-only development session, use Node.js 20.19+:

```bash
cd studio/frontend
npm ci
npm run dev
```

The full desktop app also requires the upstream Python backend and Tauri build prerequisites. Refer to the [upstream development documentation](UPSTREAM_README.md) while the WebSLM-specific setup and release process is being built. Do not use upstream Unsloth installers as WebSLM Trainer installers.

## Upstream and licenses

WebSLM Trainer is based on [unslothai/unsloth](https://github.com/unslothai/unsloth). The original author and copyright notices remain in the source. The core `unsloth/` code is under Apache-2.0 ([LICENSE](LICENSE)); `studio/` and `unsloth_cli/` are under AGPL-3.0 ([COPYING](COPYING), [studio license](studio/LICENSE.AGPL-3.0)). Other vendored components retain their own licenses. The original project documentation is kept in [UPSTREAM_README.md](UPSTREAM_README.md).

WebSLM Trainer is an independent fork and is not affiliated with or endorsed by Unsloth AI.
