# Contributing to KivyUI

Thank you for considering contributing to KivyUI! We welcome contributions from everyone. By following these guidelines, you help us maintain a high standard of quality and ensure that your contributions are easy to review and integrate.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Reporting Bugs](#reporting-bugs)
4. [Requesting Features](#requesting-features)
5. [Coding Standards](#coding-standards)
6. [Support](#support)

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment for everyone.

## How to Contribute

1. **Fork the Repository**:
   - Click the "Fork" button at the top right of the KivyUI GitHub page.
   - Clone your forked repository to your local machine:

      ```sh
      git clone https://github.com/<your-username>/KivyUI.git
      cd KivyUI
      ```

2. **Install in Editable Mode**:
   - Set up the project in editable mode using pip:

      ```sh
      pip install -e .
      ```

3. **Create a Branch**:
   - Create a new branch for your changes:

      ```sh
      git checkout -b my-feature-branch
      ```

4. **Make Your Changes**:
   - Make your changes, ensuring proper type hinting and formatting your code using the Black formatter.

      ```sh
      pip install black
      black .
      ```

5. **Commit Your Changes**:
   - Commit your changes with a clear and descriptive commit message:

      ```sh
      git add .
      git commit -m "Add feature X to KivyUI"
      ```

6. **Push Your Branch**:
   - Push your branch to your forked repository:

      ```sh
      git push origin my-feature-branch
      ```

7. **Create a Pull Request**:
   - Go to the KivyUI GitHub page and click the "New Pull Request" button.
   - Provide a detailed description of your changes, including screenshots if applicable.

## Reporting Bugs

Before reporting a bug, please:

1. **Search existing issues** on our GitHub Issues page to see if the bug has already been reported.
2. If the bug has not been reported, create a new issue using the **Bug Report** template. Provide a clear and descriptive title, a detailed description, and any relevant screenshots or code snippets.

## Requesting Features

To request a new feature:

1. **Search existing feature requests** on our GitHub Issues page to see if the feature has already been requested.
2. If the feature has not been requested, create a new issue using the **Feature Request** template. Provide a clear and descriptive title, a detailed description, and any relevant code or images.

## Coding Standards

- **Type Hinting**: Ensure all functions and methods have proper type hints.
- **Formatting**: Use the Black formatter to format your code. You can install it using `pip install black` and format your code by running `black .` in the project directory.
- **Commit Messages**: Write clear and descriptive commit messages. Follow the Conventional Commits specification.

## Support

Join the KivyUI community to get support, share your projects, and collaborate with other developers. Here are some ways you can connect with us:

- **Discord**: Join our [KivyUI Community Server](https://discord.gg/y9tqwbV5NK).
<!-- - **Stack Overflow**: Feel free to reach out on our [Stack Overflow](https://stackoverflow.com/users/16486510/el3).
- **GitHub Discussions**: Participate in discussions and ask questions in the [GitHub Discussions](https://github.com/el3/KivyUI/discussions) section.
- **YouTube - KivyUI**: Follow us on YouTube [@KivyUI](https://youtube.com/@KivyUI) for updates and announcements. -->

If you encounter any issues or have questions, feel free to reach out to the community or submit an issue on GitHub.

Thank you for your contributions and support!

Team - [KivyUI](https://github.com/el3/KivyUI)
