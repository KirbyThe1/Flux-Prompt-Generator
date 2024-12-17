# **Flux-Prompt-Generator**

**Flux Prompt Generator** is a **ComfyUI** node that provides a flexible and customizable prompt generator for generating detailed and creative prompts for image generation models.
based on the work by [Aitrepreneur](https://huggingface.co/Aitrepreneur) found here [Flux Prompt Generator python code](https://huggingface.co/Aitrepreneur/FLUX-Prompt-Generator/blob/main/app.py) and modified to work with ComfyUI by [FairyRoot](https://github.com/fairy-root)



# Flux Prompt Generator - Version 2.0 🚀  
**The Enhanced and Feature-Complete Version of the Original Flux Prompt Generator**

This is a significantly improved fork of the Version 2.0 introduces substantial enhancements, making it the most versatile and actively maintained version available for prompt generation in **ComfyUI** and other node-based systems.

---

## 🌟 **What’s New in Version 2.0?**
This fork builds upon the original tool and adds extensive new functionality, including:  

1. **Support for 30+ Customization Categories**:  
   Now you can generate highly detailed prompts with fields such as:  
   - **Roles** (e.g., "model", "photographer")  
   - **Lighting** (e.g., "soft lighting", "dramatic shadows")  
   - **Clothing** (e.g., "casual outfit", "futuristic armor")  
   - **Expressions** (e.g., "smiling warmly", "serious")  
   - **Hair Color**, **Body Markings**, **Accessories**, and many more.  

2. **Improved Prompt Generation Logic**:  
   - Attributes are **appended sequentially** for clean, readable prompts.  
   - User-defined **custom text** and **subject fields** are always prioritized.  
   - Fields marked as **"random"** automatically select valid options.

3. **User-Friendly Validation**:  
   - Only valid options are used, ensuring consistent and error-free prompts.  
   - Disabled fields are gracefully ignored.

4. **Output Example**:
   With Version 2.0, here’s an example of the prompt you can generate:

    

   **Generated Prompt**:

   


## Installation

1. **cd** to the custom_nodes folder inside of **ComfyUI** directory
2. **cmd** in the address bar, then use this command:
```
git clone https://github.com/fairy-root/Flux-Prompt-Generator.git
```

## Usage

1. **Add the "Flux Prompt Generator" node to your ComfyUI workflow.**
2. **Configure the desired parameters:**
    - **Seed:** Controls the randomness of the generator.
    - **Custom:** Add any custom text to the prompt.
    - **Subject:** Specify the main subject of the image.
    - **Artform:** Choose the desired art form (Photography, Digital Art, etc.).
    - **... (All other parameters as described in the Overview section)**

3. **Connect the output of the node to a text-to-image model (like Flux or Stable Diffusion...etc) to generate images based on the generated prompt.**

## Example

Let's say you want to generate a prompt for a portrait photograph of a woman with long hair, wearing a dress, and standing in a forest. You could configure the node with the following parameters:

- **Artform:** Photography
- **Photo Type:** Portrait
- **Default Tags:** Woman
- **Hairstyles:** Long Hair
- **Clothing:** Dress
- **Place:** Forest

The node would then generate a prompt similar to: "photography of a woman with long hair, dressed in a dress, in a forest."

## Donation

Your support is appreciated:


[(https://buymeacoffee.com/kirbythe13)]

## Author and Contact

- GitHub: [FairyRoot](https://github.com/KIRBYTHE1)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.
