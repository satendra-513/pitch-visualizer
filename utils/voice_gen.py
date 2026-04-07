import pyttsx3
import os
import uuid

def generate_voice(text: str, params: dict, output_dir: str) -> str:
    """
    Generate an audio file using pyttsx3 with modulated parameters.
    Returns the relative path to the generated file.
    """
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filename = f"voice_{uuid.uuid4().hex[:8]}.wav"
    filepath = os.path.join(output_dir, filename)
    
    try:
        engine = pyttsx3.init()
        
        # Set parameters
        engine.setProperty('rate', params['rate'])
        engine.setProperty('volume', params['volume'])
        
        # Note: pyttsx3 pitch control varies by driver. 
        # On Windows (SAPI5), it's not direct. We use rate as a proxy for 'energy'.
        
        # Save to file
        engine.save_to_file(text, filepath)
        engine.runAndWait()
        
        # Clean up engine to avoid 'runloop already started' errors in some environments
        del engine
        
        return filename
    except Exception as e:
        print(f"[Error] Voice generation failed: {e}")
        return None
