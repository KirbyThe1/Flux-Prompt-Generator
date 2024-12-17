import random
import json
import os
import re

# Load JSON files
def load_json_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), "data", file_name)
    with open(file_path, "r") as file:
        return json.load(file)

# Load categories
ARTFORM = load_json_file("artform.json")
PHOTO_TYPE = load_json_file("photo_type.json")
BODY_TYPES = load_json_file("body_types.json")
DEFAULT_TAGS = load_json_file("default_tags.json")
LIGHTING = load_json_file("lighting.json")
CLOTHING = load_json_file("clothing.json")
POSE = load_json_file("pose.json")
BACKGROUND = load_json_file("background.json")
ROLES = load_json_file("roles.json")
HAIRSTYLES = load_json_file("hairstyles.json")
ADDITIONAL_DETAILS = load_json_file("additional_details.json")
PHOTOGRAPHY_STYLES = load_json_file("photography_styles.json")
DEVICE = load_json_file("device.json")
PHOTOGRAPHER = load_json_file("photographer.json")
ARTIST = load_json_file("artist.json")
DIGITAL_ARTFORM = load_json_file("digital_artform.json")
PLACE = load_json_file("place.json")
COMPOSITION = load_json_file("composition.json")
FACE_FEATURES = load_json_file("face_features.json")
EYE_COLORS = load_json_file("eye_colors.json")
FACIAL_HAIR = load_json_file("facial_hair.json")
SKIN_TONE = load_json_file("skin_tone.json")
AGE_GROUP = load_json_file("age_group.json")
ETHNICITY = load_json_file("ethnicity.json")
ACCESSORIES = load_json_file("accessories.json")
EXPRESSION = load_json_file("expression.json")
TATTOOS_SCARS = load_json_file("tattoos_scars.json")
MAKEUP_STYLES = load_json_file("makeup_styles.json")
HAIR_COLOR = load_json_file("hair_color.json")
BODY_MARKINGS = load_json_file("body_markings.json")

class PromptGenerator:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)

    def get_choice(self, input_str, options):
        # Validate input; fallback to random if invalid
        if input_str.lower() == "disabled":
            return ""
        elif input_str.lower() == "random":
            return self.rng.choice(options)
        elif input_str in options:
            return input_str
        return self.rng.choice(options)

    def generate_prompt(self, **kwargs):
        components = []

        # Start with custom text or subject
        custom = kwargs.get("custom", "").strip()
        subject = kwargs.get("subject", "").strip()
        if custom:
            components.append(custom)
        elif subject:
            components.append(subject)

        # Append fields sequentially
        components.append(self.get_choice(kwargs.get("artform", ""), ARTFORM))
        components.append(self.get_choice(kwargs.get("photo_type", ""), PHOTO_TYPE))
        components.append(self.get_choice(kwargs.get("body_types", ""), BODY_TYPES))
        components.append(self.get_choice(kwargs.get("default_tags", ""), DEFAULT_TAGS))
        components.append(self.get_choice(kwargs.get("lighting", ""), LIGHTING))
        components.append(self.get_choice(kwargs.get("clothing", ""), CLOTHING))
        components.append(self.get_choice(kwargs.get("pose", ""), POSE))
        components.append(self.get_choice(kwargs.get("background", ""), BACKGROUND))
        components.append(self.get_choice(kwargs.get("roles", ""), ROLES))
        components.append(self.get_choice(kwargs.get("hairstyles", ""), HAIRSTYLES))
        components.append(self.get_choice(kwargs.get("additional_details", ""), ADDITIONAL_DETAILS))
        components.append(self.get_choice(kwargs.get("photography_styles", ""), PHOTOGRAPHY_STYLES))
        components.append(self.get_choice(kwargs.get("device", ""), DEVICE))
        components.append(self.get_choice(kwargs.get("photographer", ""), PHOTOGRAPHER))
        components.append(self.get_choice(kwargs.get("artist", ""), ARTIST))
        components.append(self.get_choice(kwargs.get("digital_artform", ""), DIGITAL_ARTFORM))
        components.append(self.get_choice(kwargs.get("place", ""), PLACE))
        components.append(self.get_choice(kwargs.get("composition", ""), COMPOSITION))
        components.append(self.get_choice(kwargs.get("face_features", ""), FACE_FEATURES))
        components.append(self.get_choice(kwargs.get("eye_colors", ""), EYE_COLORS))
        components.append(self.get_choice(kwargs.get("facial_hair", ""), FACIAL_HAIR))
        components.append(self.get_choice(kwargs.get("skin_tone", ""), SKIN_TONE))
        components.append(self.get_choice(kwargs.get("age_group", ""), AGE_GROUP))
        components.append(self.get_choice(kwargs.get("ethnicity", ""), ETHNICITY))
        components.append(self.get_choice(kwargs.get("accessories", ""), ACCESSORIES))
        components.append(self.get_choice(kwargs.get("expression", ""), EXPRESSION))
        components.append(self.get_choice(kwargs.get("tattoos_scars", ""), TATTOOS_SCARS))
        components.append(self.get_choice(kwargs.get("makeup_styles", ""), MAKEUP_STYLES))
        components.append(self.get_choice(kwargs.get("hair_color", ""), HAIR_COLOR))
        components.append(self.get_choice(kwargs.get("body_markings", ""), BODY_MARKINGS))

        return ", ".join(filter(None, components)).strip()

class FluxPromptGenerator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": random.randint(0, 30000)}),
                "custom": ("STRING", {"multiline": True, "default": ""}),
                "subject": ("STRING", {"default": ""}),
                "artform": (["disabled", "random"] + ARTFORM, {"default": "disabled"}),
                "photo_type": (["disabled", "random"] + PHOTO_TYPE, {"default": "disabled"}),
                "body_types": (["disabled", "random"] + BODY_TYPES, {"default": "disabled"}),
                "default_tags": (["disabled", "random"] + DEFAULT_TAGS, {"default": "disabled"}),
                "lighting": (["disabled", "random"] + LIGHTING, {"default": "disabled"}),
                "clothing": (["disabled", "random"] + CLOTHING, {"default": "disabled"}),
                "pose": (["disabled", "random"] + POSE, {"default": "disabled"}),
                "background": (["disabled", "random"] + BACKGROUND, {"default": "disabled"}),
                "roles": (["disabled", "random"] + ROLES, {"default": "disabled"}),
                "hairstyles": (["disabled", "random"] + HAIRSTYLES, {"default": "disabled"}),
                "additional_details": (["disabled", "random"] + ADDITIONAL_DETAILS, {"default": "disabled"}),
                "photography_styles": (["disabled", "random"] + PHOTOGRAPHY_STYLES, {"default": "disabled"}),
                "device": (["disabled", "random"] + DEVICE, {"default": "disabled"}),
                "photographer": (["disabled", "random"] + PHOTOGRAPHER, {"default": "disabled"}),
                "artist": (["disabled", "random"] + ARTIST, {"default": "disabled"}),
                "digital_artform": (["disabled", "random"] + DIGITAL_ARTFORM, {"default": "disabled"}),
                "place": (["disabled", "random"] + PLACE, {"default": "disabled"}),
                "composition": (["disabled", "random"] + COMPOSITION, {"default": "disabled"}),
                "face_features": (["disabled", "random"] + FACE_FEATURES, {"default": "disabled"}),
                "eye_colors": (["disabled", "random"] + EYE_COLORS, {"default": "disabled"}),
                "facial_hair": (["disabled", "random"] + FACIAL_HAIR, {"default": "disabled"}),
                "skin_tone": (["disabled", "random"] + SKIN_TONE, {"default": "disabled"}),
                "age_group": (["disabled", "random"] + AGE_GROUP, {"default": "disabled"}),
                "ethnicity": (["disabled", "random"] + ETHNICITY, {"default": "disabled"}),
                "accessories": (["disabled", "random"] + ACCESSORIES, {"default": "disabled"}),
                "expression": (["disabled", "random"] + EXPRESSION, {"default": "disabled"}),
                "tattoos_scars": (["disabled", "random"] + TATTOOS_SCARS, {"default": "disabled"}),
                "makeup_styles": (["disabled", "random"] + MAKEUP_STYLES, {"default": "disabled"}),
                "hair_color": (["disabled", "random"] + HAIR_COLOR, {"default": "disabled"}),
                "body_markings": (["disabled", "random"] + BODY_MARKINGS, {"default": "disabled"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "Prompt"

    def execute(self, **kwargs):
        generator = PromptGenerator(seed=kwargs.get("seed"))
        prompt = generator.generate_prompt(**kwargs)
        return (prompt,)

NODE_CLASS_MAPPINGS = {
    "FluxPromptGenerator": FluxPromptGenerator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FluxPromptGenerator": "Flux Prompt Generator"
}
