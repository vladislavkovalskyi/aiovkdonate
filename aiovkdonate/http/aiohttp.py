import json
from asyncio import AbstractEventLoop, get_event_loop
from typing import Optional, NoReturn

from aiohttp import TCPConnector, ClientSession


class AioHTTPClient:
	def __init__(
			self,
			loop: Optional[AbstractEventLoop] = None,
			session: Optional[ClientSession] = None
	):
		self.loop = loop or get_event_loop()
		self.session = session or ClientSession(
				connector=TCPConnector(ssl=False),
				json_serialize=json.dumps()
		)

	async def request_json(self, method: str, url: str, data: Optional[dict], **kwargs) -> dict:
		async with self.session.request(method, url, data=data, **kwargs) as response:
			return await response.json(loads=json.loads)

	async def exit(self) -> NoReturn:
		await self.session.close()
