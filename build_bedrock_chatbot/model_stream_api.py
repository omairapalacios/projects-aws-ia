
import json
import os

def stream_conversation(bedrock_client, question, system_prompt, input_model_id, input_temperature, input_top_k, messages=[], pricing_list='bedrock_pricing.json'):
    inference_config = {"temperature": input_temperature}
    
    additional_model_fields = {"top_k": input_top_k}
    
    system_prompts = [{"text": system_prompt}]
    
    message = {
        "role": "user",
        "content": [{"text": question}]
    }
    
    messages.append(message)

    response = bedrock_client.converse_stream(
        modelId=input_model_id,
        messages=messages,
        system=system_prompts,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_model_fields
    )

    stream = response.get('stream')