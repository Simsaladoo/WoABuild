import unreal

def execute():
    unreal.log("Execute!")
    unreal.MoviePipeline.get_pipeline_master_config()
    unreal.MoviePipelineQueueSubsystem.render_queue_with_executor()

execute()