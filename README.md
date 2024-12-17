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

   


## Installation

1. **cd** to the custom_nodes folder inside of **ComfyUI** directory
2. **cmd** in the address bar, then use this command:
3. Or from a Linux terminal
4. Run the following command. Restart ComfyUI
```
git clone https://github.com/kirbythe1/Flux-Prompt-Generator.git


## Usage

1. **Add the "Flux Prompt Generator" node to your ComfyUI workflow.**
2. **Configure the desired parameters:**
    - **Seed:** Controls the randomness of the generator.
    - **Custom:** Add any custom text to the prompt.
    - **Subject:** Specify the main subject of the image.
    - **Artform:** Choose the desired art form (Photography, Digital Art, etc.).
    

3. **Connect the output of the node to a text-to-image model (like Flux or Stable Diffusion...etc) to generate images based on the generated prompt.**



4. **Output Example**:
   With Version 2.0, here’s an example of the prompt you can generate:

## Example

![v2](https://github.com/user-attachments/assets/63548fac-f526-42ce-ab2b-a76a70d94339)


The node would then generate a prompt and image similar to:

![v1](https://github.com/user-attachments/assets/4b16bb9e-b60c-42d1-98ce-e02fd4962c2c)

Add the show text node to see the exact prompts that are generated

![text](https://github.com/user-attachments/assets/89153ea5-ff4f-4ff3-b6d8-5dec39388cb4)



[(https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git)]


Fast way to generate some concept images / experiments etc



## Donation

Your support is appreciated:

☕ Support My Work
If you enjoy this enhanced version and would like to support its ongoing development:
[(https://buymeacoffee.com/kirbythe13)]


To support the original author:  [FairyRoot](https://github.com/fairy-root)

USDt (TRC20): TGCVbSSJbwL5nyXqMuKY839LJ5q5ygn2uS

BTC: 13GS1ixn2uQAmFQkte6qA5p1MQtMXre6MT

ETH (ERC20): 0xdbc7a7dafbb333773a5866ccf7a74da15ee654cc

LTC: Ldb6SDxUMEdYQQfRhSA3zi4dCUtfUdsPou


## Author and Contact

- GitHub: (https://github.com/kirbythe1)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.
