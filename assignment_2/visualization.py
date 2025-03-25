
def save_video_of_model(env, model=None, suffix="", num_episodes=10):
    """
    Record a video that shows the behavior of an agent following a model 
    (i.e., policy) on the input environment
    """
    from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(300, 300))
    display.start()

    obs, _ = env.reset()
    prev_obs = obs
    env_name = env.unwrapped.spec.id
    
    filename = env_name + suffix + ".mp4"
    recorded_frames = []

    counter = 0
    done = False
    num_runs = 0
    returns = 0
    while num_runs < num_episodes:
        frame = env.unwrapped._render_frame("rgb_array")
        recorded_frames.append(frame)

        input_obs = obs

        if model is not None:
            action = model(input_obs)
        else:
            action = env.action_space.sample()

        prev_obs = obs
        obs, reward, done, truncated, info = env.step(action)
        counter += 1
        returns += reward
        if done or truncated:
            num_runs += 1
            obs, _ = env.reset()

    clip = ImageSequenceClip(recorded_frames, fps=8)
    clip.write_videofile(filename, logger=None)
            
    print("Successfully saved {} frames into {}!".format(counter, filename))
    return filename, returns / num_runs

def play_video(filename, width=None):
    """Play the input video"""

    from base64 import b64encode
    mp4 = open(filename,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    html = """
    <video width=400 controls>
          <source src="%s" type="video/mp4">
    </video>
    """ % data_url
    return  html
