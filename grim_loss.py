from grim_loss import grim_loss
total_loss = task_loss + 10.0 * grim_loss(embeddings, step)
